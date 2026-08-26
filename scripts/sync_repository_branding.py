#!/usr/bin/env python3
"""Safely apply JAHID repository presentation metadata across an account.

The script intentionally does not replace LICENSE, NOTICE, COPYRIGHT, attribution,
or trademark files. README changes are opt-in through the ORIGINAL_REPOSITORIES or
MODIFIED_REPOSITORIES environment variables.
"""

from __future__ import annotations

import os
import sys
from typing import Any

import requests

API = "https://api.github.com"
OWNER = "mdjahid11978-design"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("JAHID_REPO_SYNC_TOKEN")

if not TOKEN:
    raise SystemExit("Set GITHUB_TOKEN or JAHID_REPO_SYNC_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def split_env(name: str) -> set[str]:
    return {x.strip() for x in os.environ.get(name, "").split(",") if x.strip()}


ORIGINAL = split_env("ORIGINAL_REPOSITORIES")
MODIFIED = split_env("MODIFIED_REPOSITORIES")
DRY_RUN = os.environ.get("DRY_RUN", "true").lower() not in {"0", "false", "no"}


def request(method: str, path: str, **kwargs: Any) -> requests.Response:
    response = requests.request(method, f"{API}{path}", headers=HEADERS, timeout=30, **kwargs)
    response.raise_for_status()
    return response


def classify(repo: dict[str, Any]) -> str:
    name = repo["name"]
    if name in ORIGINAL:
        return "ORIGINAL"
    if name in MODIFIED:
        return "MODIFIED"
    if repo.get("fork"):
        return "FORK"
    if repo.get("archived"):
        return "ARCHIVE"
    return "UNKNOWN"


def branding(classification: str) -> str:
    labels = {
        "ORIGINAL": "BUILT BY JAHID",
        "MODIFIED": "ADAPTED & MAINTAINED BY JAHID",
        "FORK": "MAINTAINED BY JAHID · UPSTREAM ATTRIBUTION PRESERVED",
        "ARCHIVE": "ARCHIVED · JAHID REPOSITORY",
        "UNKNOWN": "JAHID REPOSITORY · PROVENANCE REVIEW REQUIRED",
    }
    return labels[classification]


def metadata(repo: dict[str, Any], classification: str) -> str:
    return f'''# JAHID Repository Metadata\n\n**Repository:** `{repo["full_name"]}`  \n**Classification:** `{classification}`  \n**Presentation:** **{branding(classification)}**  \n**Platform:** [JAHIDS.AI](https://github.com/{OWNER}/jahids.ai)\n\nThis file records repository presentation metadata. It does not replace the repository's license, copyright notices, upstream attribution, trademarks, or third-party terms.\n\n## Operating standard\n\n- Keep project-specific technical documentation in `README.md` and `docs/`.\n- Separate implemented, tested, deployed, and planned capabilities.\n- Preserve upstream legal and attribution material.\n- Treat model output as untrusted input.\n- Use explicit authorization and policy checks for protected actions.\n'''


def get_content(repo: str, path: str) -> dict[str, Any] | None:
    response = requests.get(f"{API}/repos/{OWNER}/{repo}/contents/{path}", headers=HEADERS, timeout=30)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def put_file(repo: str, path: str, content: str, message: str, sha: str | None = None) -> None:
    import base64

    payload = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    if DRY_RUN:
        print(f"DRY-RUN {repo}: {path}")
        return
    request("PUT", f"/repos/{OWNER}/{repo}/contents/{path}", json=payload)
    print(f"UPDATED {repo}: {path}")


def main() -> None:
    page = 1
    while True:
        repos = request("GET", f"/user/repos?per_page=100&page={page}&affiliation=owner").json()
        if not repos:
            break
        for repo in repos:
            if repo["owner"]["login"] != OWNER:
                continue
            name = repo["name"]
            classification = classify(repo)
            metadata_path = "JAHID_REPOSITORY.md"
            existing = get_content(name, metadata_path)
            put_file(
                name,
                metadata_path,
                metadata(repo, classification),
                f"docs: add JAHID repository metadata ({classification.lower()})",
                existing.get("sha") if existing else None,
            )

            # README presentation is deliberately limited to explicitly classified
            # original/modified repositories. Unknown, forked, archived, and upstream
            # repositories receive metadata only so source identity remains intact.
            if classification not in {"ORIGINAL", "MODIFIED"}:
                continue

            readme = get_content(name, "README.md")
            if not readme:
                continue
            import base64

            current = base64.b64decode(readme["content"]).decode("utf-8")
            marker = "<!-- JAHID-BRANDING:START -->"
            if marker in current:
                continue
            end = "<!-- JAHID-BRANDING:END -->"
            header = f'''{marker}\n\n<div align="center">\n\n# {name}\n\n### {branding(classification)}\n\n**AI · AGENTS · ASSISTANTS · SYSTEMS · ENGINEERING**\n\n[![Built by Jahid](https://img.shields.io/badge/BUILT%20BY-JAHID-f5a623)](https://github.com/{OWNER})\n[![JAHIDS.AI](https://img.shields.io/badge/JAHIDS.AI-CANONICAL-111827)](https://github.com/{OWNER}/jahids.ai)\n\n</div>\n\n{end}\n\n---\n\n'''
            put_file(name, "README.md", header + current, f"docs: apply JAHID README branding ({classification.lower()})", readme["sha"])
        page += 1


if __name__ == "__main__":
    main()
