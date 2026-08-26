# Repository Branding Automation

This repository is the source of truth for the JAHID GitHub presentation standard.

## Safe rollout model

The account contains original projects, forks, upstream projects, experiments, documentation mirrors, and imported code. Automation must classify before changing files.

```text
List repositories
    ↓
Read repository metadata
    ↓
Classify provenance
    ↓
Inspect README / legal files
    ↓
Generate JAHID metadata
    ↓
Apply branding only where policy permits
    ↓
Validate Markdown and links
    ↓
Commit a small change
    ↓
Record result
```

## Classification

```text
ORIGINAL
MODIFIED
FORK
UPSTREAM
EXPERIMENT
DOCUMENTATION
ARCHIVE
UNKNOWN
```

`UNKNOWN` repositories must not receive ownership language automatically.

## Safe files

Automation may add or update repository-specific presentation files such as:

- `JAHID_REPOSITORY.md`
- `PROVENANCE.md`
- `BRANDING.md`
- `.github/ISSUE_TEMPLATE/*`
- `.github/PULL_REQUEST_TEMPLATE.md`

README changes require inspection because an existing README may contain upstream material or project-specific structure.

## Never overwrite automatically

- `LICENSE`
- upstream copyright notices
- upstream NOTICE files
- third-party attribution files
- trademark notices
- security policies from upstream projects
- generated vendor code

## Repository result record

Each automation run should record:

```json
{
  "repository": "owner/name",
  "classification": "ORIGINAL",
  "default_branch": "main",
  "readme_changed": true,
  "files_added": [],
  "files_skipped": [],
  "reason": "",
  "commit": ""
}
```

## Credentials

Cross-repository automation requires an explicitly authorized GitHub App or token with the minimum required permissions. Never place credentials in source files, README files, workflow YAML, or generated artifacts.

## Operating rule

The target is consistent presentation across the account while preserving each repository's technical history and legal boundaries.
