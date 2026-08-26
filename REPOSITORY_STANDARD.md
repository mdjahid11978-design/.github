# mdjahid11978-design — Repository Standard

**Account documentation baseline:** 2026-08-26

This standard defines the Markdown baseline for repositories controlled by `mdjahid11978-design`.

## Required repository identity

Every maintained repository should clearly state:

- repository name
- purpose
- project status
- owner/maintainer attribution
- upstream relationship when applicable
- license
- provenance boundary

## README baseline

Where appropriate, README files should contain:

1. Project overview
2. Status
3. Features
4. Architecture
5. AI / agents / skills / tools
6. Installation
7. Configuration
8. Usage
9. Project structure
10. API or interfaces
11. Security
12. Testing
13. Deployment
14. Documentation
15. Roadmap
16. Contributing
17. License
18. Third-party attribution
19. Ownership and provenance

## Standard Markdown files

Use these where relevant to the project:

- `README.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `LICENSE` or `LICENSE.md`
- `NOTICE.md`
- `ATTRIBUTIONS.md`
- `THIRD_PARTY.md`
- `COPYRIGHT.md`
- `OWNERSHIP.md`
- `GOVERNANCE.md`
- `AI_GOVERNANCE.md`
- `AGENT_GOVERNANCE.md`
- `HUMAN_OVERSIGHT.md`
- `MODEL_POLICY.md`
- `TOOL_POLICY.md`
- `PROVENANCE.md`
- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `ROADMAP.md`

Do not add irrelevant files to a small upstream project merely for appearance. Apply the smallest useful set.

## Attribution classes

| Class | Repository presentation |
|---|---|
| Original project | `BUILT BY JAHID` |
| Modification/fork | `ADAPTED & MAINTAINED BY JAHID` |
| Upstream project | `MAINTAINED BY JAHID · UPSTREAM ATTRIBUTION PRESERVED` |
| Third-party component | Preserve original license and attribution |
| JAHIDS.AI project | Apply JAHIDS.AI governance and provenance records |

## Legal rule

GitHub account ownership does not mean ownership of every repository, file, dependency, model, dataset, or upstream project. Existing licenses remain effective. Do not replace or remove upstream legal notices.

## Documentation truthfulness

Markdown must distinguish:

- planned
- implemented
- tested
- deployed
- verified production

Do not claim autonomous, production, security, legal, or ownership status without evidence.

## Engineering standard

- Keep secrets out of Git.
- Use reproducible builds where practical.
- Record versions and source commits for releases.
- Keep deployment artifacts traceable.
- Maintain rollback information for production systems.
- Use least-privilege access.
- Keep changes reviewable.

## Account-wide target

The account should progressively classify repositories as:

`ORIGINAL | MODIFIED | UPSTREAM | FORK | EXPERIMENT | ARCHIVE | DOCUMENTATION | UNKNOWN`

Classification must be evidence-based.
