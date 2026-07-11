---
name: update-runbook
description: Use when the ENS Meta-Governance runbook needs refreshing — after a new ENS proposal (on-chain EP or Snapshot social/constitutional vote), a steward election or term transition, a change to a multisig / Security Council / treasury setup, or when an OPEN-QUESTIONS item becomes resolvable.
---

# Update the ENS Meta-Gov Runbook

## Overview

Refresh the docs from canonical sources, keeping the repo's founding discipline:

> **Every change carries a source link. Never invent or estimate a number, address, date, rate, or name. Anything you cannot verify from a source goes to [OPEN-QUESTIONS.md](../../../OPEN-QUESTIONS.md) — never into the docs as fact.**

The focus is operational (how things are run), not financial (live dollar values — link the dashboards instead).

## When to use

- A new on-chain Executable Proposal or Snapshot social/constitutional vote.
- A steward election result or a term transition (a new term → the archive).
- A multisig, Security Council, or treasury-automation/fee change.
- An OPEN-QUESTIONS item became answerable (e.g., election results after the vote).

Not for prose polish or restructuring — that's an ordinary PR.

## Data sources (canonical)

| Source | Where | Use it for |
|--------|-------|-----------|
| anticapture MCP (`dao=ens`) | tools: `proposals`, `offchainProposals`, `searchProposals`, `votingPowers`, treasury | structured proposal / vote / treasury data |
| ENS forum | discuss.ens.domains (append `.json`) | proposal lifecycle, elections, funding, comp, reports |
| ENS docs | docs.ens.domains/dao (Constitution, wg/rules, stewards, proposals/`<n>`) | rules and per-EP pages |
| Snapshot | snapshot.box/#/s:ens.eth | social/constitutional votes + results |
| Tally | tally.xyz/gov/ens | on-chain executables, status, IDs |
| Safe Tx Service | safe-transaction-mainnet.safe.global/api/v1/safes/`{addr}`/ | multisig owners + threshold (verify before editing `addresses.md`) |
| ens-contracts deployments / Etherscan | github.com/ensdomains/ens-contracts/wiki · etherscan.io | contract addresses |
| karpatkey reports | reports.kpk.io/ens | endowment ops (link, don't transcribe values) |

## Source → file map

| Change | Update |
|--------|--------|
| New rule/structure/process proposal | `reference/governance-history.md` (timeline) + `01-governance/proposals.md` (lifecycle/types/EP numbering) + the relevant section file |
| New term | `05-terms/term-0N.md` + `05-terms/README.md` matrix + `reference/changelog.md` |
| Steward election result / role change | `01-governance/elections.md` (election outcome), `01-governance/stewards-and-roles.md`, `directory.md`, the term file |
| Multisig / threshold change | `02-contracts-and-multisigs/addresses.md` + `multisigs.md` |
| Treasury automation / fee change | `03-treasury-and-endowment/treasury-automation.md`, `treasury-manager-fees.md`, `endowment*.md` |
| Endowment-permission ("Update #N") change | `03-treasury-and-endowment/endowment-permissions.md` + `addresses.md` |
| Security Council change | `02-contracts-and-multisigs/security-council.md` + `addresses.md` |
| Question resolved | remove from `OPEN-QUESTIONS.md`, add the cited fact to its file |

`addresses.md` is the single source of truth for addresses — other files **link** to it, they don't re-list.

## Procedure

1. **Baseline** — read `reference/changelog.md`, the `_as of_` dates, and `OPEN-QUESTIONS.md`. Know what's already documented and what's pending.
2. **Gather** — for breadth, dispatch parallel subagents (one per source/topic). Each returns *cited facts only* and flags gaps; instruct them to never assume. (This mirrors how the repo was first built.)
3. **Diff** — list concrete changes per file from the gathered facts.
4. **Verify structural facts on-chain** — confirm any address / threshold / role via Safe API or Etherscan *before* editing `addresses.md`.
5. **Apply** — make the edits under the discipline below; keep `addresses.md` canonical.
6. **Record** — update `reference/changelog.md` and bump the `_as of <date>_` stamps you touched.
7. **Validate** — run `python3 scripts/verify.py` (links, placeholders, address consistency). Fix anything it reports.

## Non-negotiable discipline

- Cite every concrete claim with a source link.
- Never invent or estimate a number, address, date, rate, or name. No source → it goes to `OPEN-QUESTIONS.md`, not the docs.
- Operational over financial — link live dashboards rather than hardcoding values.
- Succinct and high-signal. No filler.
- Mark superseded items as historical; don't silently erase the record.

## Red flags — STOP and route to OPEN-QUESTIONS instead

- About to type a number/address/date you didn't pull from a source this session.
- "It's probably still 3/4" · "the date is likely…" · "the signers are presumably…"
- Editing `addresses.md` without a Safe API / Etherscan check.
- Writing any claim that has no citation link.
- A leftover `<DATE>` / `<ID>` / `<owner-N>` placeholder — fill it with a verified value or the item isn't done. `scripts/verify.py` flags these.

## Common mistakes

- Re-listing addresses in a section file instead of linking `addresses.md` (causes divergence).
- Asserting an election outcome, threshold change, or rate before it's on-chain / in a source — record it as pending instead.
- Deleting a superseded proposal's record instead of marking it historical in `changelog.md`.
