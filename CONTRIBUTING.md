# Contributing to this runbook

This is the operational runbook for the ENS DAO [Meta-Governance Working Group](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) — the sole operational Working Group as of Term 7. It documents **how** Meta-Gov runs the DAO: structure, contracts, treasury, and procedures.

## How to propose an edit

1. **Open a PR** against this repo. Keep changes scoped — one topic per PR.
2. **Cite every concrete claim** with an inline markdown link to a primary source (docs.ens.domains, the [governance-docs repo](https://github.com/ensdomains/governance-docs), the forum, Etherscan, or the Safe API).
3. **Single source of truth — do not restate volatile facts.** Each fact has exactly one owner file; everywhere else links to it, never re-states the value:
   - **Addresses & Safe thresholds** → [`02-contracts-and-multisigs/addresses.md`](02-contracts-and-multisigs/addresses.md)
   - **Dates, rates, member lists, and EP-series** (election dates, compensation rates, council/steward rosters, "Update #N" and EP numbering) → their owner section file.

   This applies to addresses, thresholds, dates, rates, member lists, and EP-series. Link to the owner; never re-list these elsewhere, to avoid divergence.
4. **Use relative links** between files in this repo.

### Exception: full addresses in runbook steps

A full `0x…` address **may** be inlined in a `04-runbook/` procedure step where a signer reads it at the point of signing — copying an address out of a linked table is itself an error surface. When you do, add a note to **verify against [`02-contracts-and-multisigs/addresses.md`](02-contracts-and-multisigs/addresses.md)** so the canonical table stays the arbiter. This is the only place a raw address is duplicated on purpose.

## Ownership

The Meta-Governance stewards own this runbook. PRs are reviewed and merged by the stewards (the most recent confirmed roster is on [docs.ens.domains/dao/stewards](https://docs.ens.domains/dao/stewards)). Substantive governance-process edits should track the canonical [Working Group Rules](https://docs.ens.domains/dao/wg/rules/).

## Validation

`scripts/verify.py` runs in **CI** on every PR — it checks relative links, unfilled template tokens, and address consistency against [`02-contracts-and-multisigs/addresses.md`](02-contracts-and-multisigs/addresses.md). Run it locally (`python3 scripts/verify.py`) before pushing; a red check blocks merge.

## Freshness policy

| When | What to do |
| --- | --- |
| **Each new term** | Re-verify stewards, Lead Steward, Secretary (or its absence), compensation rates, and the multisig threshold against the term's nomination/funding sources. See [`changelog.md`](reference/changelog.md). |
| **On any contract change** | Re-verify the affected addresses against the [ens-contracts deployments wiki](https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments) and the [Safe Transaction Service](https://api.safe.global/) (owners + threshold), then update [`02-contracts-and-multisigs/addresses.md`](02-contracts-and-multisigs/addresses.md). |
| **Time-sensitive values** (treasury size, current stewards) | Prefer linking the live source over hardcoding. Where a number is unavoidable, stamp it `_as of YYYY-MM-DD_`. |

## Unresolved items

Anything not yet confirmed by a primary source must **not** be asserted as fact. Record it in `OPEN-QUESTIONS.md` with the question and the source that would resolve it, and reference it inline with a brief blockquote:

> ⚠️ **Open question:** … (see `OPEN-QUESTIONS.md`)

Resolve and remove the entry once a primary source confirms it.
