# WG Funding Request & Runway

How Meta-Gov funds itself each term, and how the DAO's operating runway is kept topped up. These are **two distinct flows**:

| Flow | Trigger | Direction | Cadence |
|---|---|---|---|
| **WG Safe top-up** | A funding **EP** passes | `wallet.ensdao.eth` (Timelock) → [Meta-Gov Safe](../02-contracts-and-multisigs/addresses.md) | Per term |
| **Operating runway top-up** | Automated (EP6.39) | Endowment → Timelock | When below threshold (checked quarterly) |

The WG Safe top-up is the funding-request procedure below. The operating runway top-up is fully automated. See [Operating runway top-ups](#operating-runway-top-ups-automated).

## Funding-request procedure

The pattern is **social proposal → collective executable**: the WG posts a funding request, then the approved amount moves from the Timelock to the WG Safe via an on-chain executable ([Funding Requests, ENS Basics](https://basics.ensdao.org/funding-requests)).

1. **Set compensation standards** before the nomination window opens (a Meta-Gov duty per the [Meta-Gov mandate](https://basics.ensdao.org/metagovernance-wg)). Current Term 7 rates live in [term-07.md](../05-terms/term-07.md).
2. **Post the funding request.** `[X.Y.Z] [Social] Funding Request: ENS Meta-Governance Working Group Term X` in the [Meta-Governance category](https://discuss.ens.domains/c/meta-governance/28). Some terms split this into ~April and ~October windows; the [WG Rules](https://docs.ens.domains/dao/wg/rules/) funding cadence is quarterly (Jan/Apr/Jul/Oct).
3. **Collective executable.** The approved amount streams from the Timelock to the [Meta-Gov Safe](../02-contracts-and-multisigs/addresses.md) via the executable proposal flow. See the [proposal lifecycle](../01-governance/proposals.md).
4. **Disburse & reallocate.** Stewards disburse to initiatives and may reallocate within the approved budget under **WG Rule 10.5**, subject to Constitution Article III ([rules](https://docs.ens.domains/dao/wg/rules/); [constitution](https://docs.ens.domains/dao/constitution/)).

## Per-term DAO → Safe top-ups

Each term the WG's spending envelope is set by an inbound transfer from `wallet.ensdao.eth` (executed by the Governor) into the Meta-Gov Safe: USDC for compensation, plus ENS for token distribution. Examples: **100,000 ENS (2025-05)** and **150,000 ENS (2024-07)** ([Safe Tx Service](https://app.safe.global/)).

**When to request a new funding EP:** when the term's budget is set, or when the Safe's USDC balance won't cover upcoming [monthly compensation](monthly-compensation.md) runs. Requests follow the per-term forum cadence in step 2 above; see [calendar.md](calendar.md).

### Typical line items

| Line item | Notes |
|---|---|
| Steward compensation | Per-steward monthly USDC + 2-year-vested ENS |
| Lead Steward uplift | Higher monthly rate + vested ENS |
| Secretary compensation | Paid by Meta-Gov when the role is filled ([rules](https://docs.ens.domains/dao/wg/rules/)) |
| Scribe / operational reserve | Covers WG running costs |

Current per-role rates: [term-07.md](../05-terms/term-07.md). For scale, WG steward + secretary compensation ran **~$294k USDC for 9 people over 6 months** in a prior term ([treasury facts](https://basics.ensdao.org/funding-requests)). The monthly compensation batch is a single USDC `multiSend` from the Meta-Gov Safe. See [monthly-compensation.md](monthly-compensation.md).

## Operating runway top-ups (automated)

Since **EP6.39 Treasury Flow Automation**, karpatkey replenishes the DAO's operating runway (a 6-month USDC buffer in the Timelock) **without a vote**, within a tightly scoped Zodiac permission, deprecating the old one-off "transfer USDC from endowment to `wallet.ensdao.eth`" votes. Full policy, constraints, and deprecated flows: [../03-treasury-and-endowment/treasury-automation.md](../03-treasury-and-endowment/treasury-automation.md).

> ⚠️ **Open question:** Whether the Jan/Apr/Jul/Oct quarterly funding windows shift with the new July-anchored Term 7 cycle is not stated in the sources.
