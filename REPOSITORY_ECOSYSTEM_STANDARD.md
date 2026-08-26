# JAHID GitHub Repository Ecosystem Standard

This repository defines the account-wide management standard for `mdjahid11978-design`.

## Canonical platform

`mdjahid11978-design/jahids.ai` is the canonical JAHIDS.AI integration platform.

## Repository classes

- **Original** — original work owned by the project author; may use JAHID branding where accurate.
- **Modified/Fork** — changes maintained by Jahid while preserving upstream attribution and license.
- **Upstream** — external project mirrored or maintained in the account; upstream legal identity remains authoritative.
- **Documentation/Reference** — documentation or reference material; no ownership claim over source material.
- **Experimental** — temporary or exploratory repository.
- **Archived** — retained for history and not promoted into production.

## Required lifecycle

`INVENTORY → CLASSIFY → PROVENANCE → SECURITY → BUILD → TEST → INTEGRATE → RUNTIME VERIFY → PROMOTE`

## Branding

Use JAHID branding only when it accurately describes the relationship to the repository. Branding never replaces a repository's existing copyright, license or attribution requirements.

## JAHIDS.AI integration

A repository can become a JAHIDS.AI capability only after:

- provenance is recorded;
- license compatibility is reviewed;
- dependencies are identified;
- security review passes;
- build/tests pass;
- an adapter or integration boundary exists;
- runtime behavior is verified;
- the capability is registered in JAHIDS.AI.

No repository is considered LIVE from source metadata alone.
