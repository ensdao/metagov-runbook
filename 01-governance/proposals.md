# Proposals

Every proposal moves through three phases ([governance process](https://docs.ens.domains/dao/governance/process/), [submission guide](https://docs.ens.domains/dao/proposals/submit/)), then forks by type: social votes finish on Snapshot; executable proposals run on-chain through the Governor and Timelock.

```
Temp Check ──▶ Draft Proposal (governance-docs PR / EP) ──┬─▶ Snapshot (social) ──▶ done
                                                          └─▶ Governor / Tally ──▶ 2-day timelock ──▶ execution
```

## Lifecycle

**1 · Temperature Check**: an optional, informal poll in the discuss.ens.domains "Temperature Check" category to gauge sentiment before drafting.

**2 · Draft Proposal (governance-docs PR → EP)**: a pull request to the [governance-docs repo](https://github.com/ensdomains/governance-docs) using the relevant template (executable / social / constitutional). When merged, the proposal is assigned an **EP number** (see [EP numbering](#ep-numbering-convention) below).

**3 · Active Proposal & Voting**: the vote runs at the venue and thresholds set by the proposal type (below).

## Types & thresholds

| Type | Venue | Proposal threshold | Quorum | Approval | Vote period | After approval |
| --- | --- | --- | --- | --- | --- | --- |
| **Social** | [Snapshot](https://snapshot.box/#/s:ens.eth) (off-chain) | n/a | 1% | 50% | ~5 days | Binding socially; no on-chain execution. |
| **Executable** | ENS Governor via [Tally](https://www.tally.xyz/gov/ens) (on-chain) | 100,000 ENS delegated to propose | 1% | 50% | ~7 days on-chain | Queue, then minimum **2-day timelock**, then execution. |
| **Constitutional** | Snapshot (special social proposal, with a diff) | n/a | 1% | **Two-thirds** | n/a | Amends the [Constitution](constitution.md). |

A **Constitutional amendment** is a special social proposal carrying a diff of the proposed change; it keeps the 1% quorum but raises the approval bar to two-thirds, matching the [Constitution's Article V](constitution.md) amendment rule (two-thirds majority, at least 1% of tokens participating).

## Timelock & execution

Approved executable proposals are queued, then held by the [ENS Timelock](../02-contracts-and-multisigs/addresses.md) for a **minimum 2-day (172,800s) delay** before execution ([process](https://docs.ens.domains/dao/governance/process/)). All funds leave the Timelock only after this delay. During this window the Security Council can cancel (veto) a queued malicious operation. See [security-council.md](../02-contracts-and-multisigs/security-council.md).

## EP numbering convention

Merged proposals are assigned an **EP number** of the form **EP N.M**, where the **leading digit N is the term number** and M is the proposal index within that term ([EP numbering](https://basics.ensdao.org/executable-proposals)). For example, proposals submitted in Q1/Q2 2023 (Term 3) begin with `3` (EP3.x), and Q3/Q4 2023 (Term 4) begin with `4` (EP4.x). Term 7 proposals are expected to use the `7` prefix.

> ⚠️ **Open question:** The EP-prefix-to-term mapping is explicitly confirmed only for Term 3 (EP3.x) and Term 4 (EP4.x). Other terms, including Term 7 = EP7.x, are inferred from the consistent leading-digit pattern; no EP7.x proposal is confirmed yet.
