# ENS Meta-Governance Runbook

[![verify-docs](https://github.com/ensdao/metagov-runbook/actions/workflows/verify.yml/badge.svg)](https://github.com/ensdao/metagov-runbook/actions/workflows/verify.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey.svg)](LICENSE)
![status: draft](https://img.shields.io/badge/status-draft%20·%20pending%20steward%20review-orange)

Documentation and operational runbook for the **ENS DAO Meta-Governance Working Group** — the context needed to *run* the group: how the DAO is governed, what Meta-Gov controls (multisigs, contracts, treasury), the critical proposals that shaped the rules, the recurring operational routines, and a per-term institutional-memory archive.

Public, plain-markdown, navigable from the GitHub UI. The emphasis is **operational** — how things are managed and run, not financial analysis. _Current as of 2026-06-20._

> **Current state:** ENS is transitioning into **Term 7 (1 Jul 2026 – 30 Jun 2027)**. Following the "ENS Retro," Meta-Governance is becoming the **sole Working Group** (Ecosystem and Public Goods dissolved), and the term cycle shifted to a July–June anchor. Items still in motion are tracked in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

> ## 🚨 Emergency
> - **A malicious proposal is queued and could execute** → [Security Council emergency veto](02-contracts-and-multisigs/security-council.md). The 4-of-8 council can cancel a queued Timelock operation inside its delay window.
> - **Suspected phishing / address-poisoning at signing time** → [verification & safety](04-runbook/verification-and-safety.md). Do not sign until every recipient is verified.

## Start here

New steward? Begin with **[onboarding](04-runbook/onboarding.md)** — it walks you from governance basics to your first signature in order.

## Sections

| Section | What's inside |
|---|---|
| [01 · Governance](01-governance/) | Working groups, the Constitution, [stewards & roles](01-governance/stewards-and-roles.md), [elections](01-governance/elections.md), the [proposal lifecycle & types](01-governance/proposals.md) |
| [02 · Contracts & multisigs](02-contracts-and-multisigs/) | Governance contract hierarchy, the multisigs, the [Security Council](02-contracts-and-multisigs/security-council.md), ENS-protocol control, and the [⭐ canonical address table](02-contracts-and-multisigs/addresses.md) |
| [03 · Treasury & endowment](03-treasury-and-endowment/) | Revenue flow, the [EP 6.39 treasury automation](03-treasury-and-endowment/treasury-automation.md), the karpatkey endowment, the SPP, spending controls |
| [04 · Runbook](04-runbook/) | Step-by-step procedures for the recurring on-chain operations (table below) |
| [05 · Terms archive](05-terms/) | Per-term record (Terms 0–7): stewards, funding, compensation, activity |
| [Reference](reference/) | [Critical-proposals timeline](reference/governance-history.md), [canonical links](reference/resources.md), [glossary](reference/glossary.md), [structural changelog](reference/changelog.md) |

Also: [directory.md](directory.md) (who's-who + how to reach them) · [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) (unverified / in-motion items).

## Runbook

Start with **[verification & safety](04-runbook/verification-and-safety.md)** — read it before approving any transaction.

| Procedure | When | File |
|---|---|---|
| Verification & anti-phishing | Every signature | [verification-and-safety.md](04-runbook/verification-and-safety.md) |
| Onboarding a new steward/signer | On joining | [onboarding.md](04-runbook/onboarding.md) |
| Monthly compensation run | Monthly (1st–2nd) | [monthly-compensation.md](04-runbook/monthly-compensation.md) |
| Funding & runway top-ups | Per term / funding window | [funding-request.md](04-runbook/funding-request.md) |
| Token distribution (Hedgey) | Per governing EP | [token-distribution.md](04-runbook/token-distribution.md) |
| Treasury-manager fees (karpatkey) | Monthly (automated) | [treasury-manager-fees.md](04-runbook/treasury-manager-fees.md) |
| Steward elections | Annual (term transition) | [01-governance/elections.md](01-governance/elections.md) |
| Endowment-permission updates | Per governing EP | [03-treasury-and-endowment/endowment-permissions.md](03-treasury-and-endowment/endowment-permissions.md) |
| Security Council emergency veto | Emergency only | [02-contracts-and-multisigs/security-council.md](02-contracts-and-multisigs/security-council.md) |
| Signer good-practices | Ongoing | [signers.md](04-runbook/signers.md) |
| Annual governance calendar | Reference | [calendar.md](04-runbook/calendar.md) |

## How to use & contribute

- Every concrete claim links to its source (forum, docs, Snapshot, Tally, Etherscan, Safe). **Verify on-chain before signing** — see [verification & safety](04-runbook/verification-and-safety.md).
- Unverified or in-motion items are **not asserted** — they live in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) for resolution.
- Edits go through pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC BY 4.0](LICENSE).
