# JAHID Repository System

## Identity

- GitHub owner: `mdjahid11978-design`
- Canonical platform: `JAHIDS.AI`
- Canonical repository: `mdjahid11978-design/jahids.ai`
- Maintainer identity: `Jahid`

## Purpose

This file defines the repository-wide operating standard for projects owned or maintained by `mdjahid11978-design`.

## Repository classes

### 1. Original project
Use:

> BUILT BY JAHID

Apply the full JAHIDS.AI documentation, engineering, security, CI, governance and provenance standard when appropriate.

### 2. Fork or modified upstream project
Use:

> ADAPTED & MAINTAINED BY JAHID

Preserve upstream copyright, license, notices and attribution. Document modifications separately.

### 3. Upstream mirror or imported project
Use:

> MAINTAINED BY JAHID · UPSTREAM ATTRIBUTION PRESERVED

Do not replace upstream legal files or claim upstream authorship.

### 4. Third-party dependency or documentation mirror
Preserve the original license and attribution. Add JAHID branding only where it does not alter the upstream legal meaning.

## Standard repository files

Add only files appropriate to the repository:

```text
README.md
LICENSE
LICENSE.md
COPYRIGHT.md
OWNERSHIP.md
NOTICE.md
ATTRIBUTIONS.md
THIRD_PARTY.md
TRADEMARKS.md
REGISTRATION.md
LICENSE_REGISTRY.md
CITATION.cff
GOVERNANCE.md
AI_GOVERNANCE.md
AGENT_GOVERNANCE.md
HUMAN_OVERSIGHT.md
MODEL_POLICY.md
TOOL_POLICY.md
SECURITY.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
CHANGELOG.md
.github/workflows/ci.yml
.github/workflows/security.yml
.github/workflows/dependency-review.yml
.github/workflows/release.yml
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
```

## JAHIDS.AI runtime standard

For executable AI systems, the preferred production path is:

```text
inspect
→ build
→ typecheck
→ test
→ security
→ database
→ redis
→ llm
→ memory
→ agents
→ tools/mcp
→ worker
→ scheduler
→ observability
→ adapters
→ readiness
→ recovery
→ canary
→ promotion
```

A required failed gate blocks promotion.

## LIVE rule

A repository must not be labeled `LIVE`, `24/7`, `production-ready`, or `healthy` solely from source code. Production claims require an actual deployment and successful runtime evidence.

Minimum runtime evidence for an AI service:

- liveness
- readiness
- database persistence
- Redis/queue connectivity
- LLM connectivity
- memory read/write/retrieval
- agent execution
- tool/MCP execution
- worker heartbeat
- scheduler heartbeat
- observability telemetry
- security checks
- recovery/rollback test

## Continuous improvement

Automated maintenance may inspect, test, evaluate, propose, patch, and validate changes. Production promotion remains gated by policy, testing, security checks and recovery evidence.

## Security

Never commit secrets, production credentials, private keys, tokens, or personal data. Use repository/environment secrets or an external secret manager.

## Provenance

Every repository should be traceable to its source, license, ownership class, modifications and major dependencies.

## Canonical platform

All original JAHIDS.AI platform work belongs under:

`mdjahid11978-design/jahids.ai`

**Built and maintained by Jahid.**
