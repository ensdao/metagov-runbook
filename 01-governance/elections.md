# Steward Elections

Stewards are chosen by **self-nomination followed by a ranked-choice (Copeland) election** on Snapshot ([WG Rules](https://docs.ens.domains/dao/wg/rules/)). Three stewards are elected per Working Group; for Term 7 (2026) Meta-Governance is the **sole** Working Group ([Path forward vote](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)). This page is the source of truth for election mechanics and dates.

## Mechanics

| Step | Detail |
| --- | --- |
| **Nomination** | Self-nomination during the nomination window. |
| **Vote threshold** | A nominee must clear **≥10,000 supporting votes** during the nomination window to reach the ballot (WG Rule 4.4). |
| **Election** | **Ranked-choice (Copeland)** vote on [Snapshot (`s:ens.eth`)](https://snapshot.box/#/s:ens.eth) over a 120-hour window; the top 3 by score are seated. |
| **Seats** | **Three stewards** elected per Working Group. |
| **Appointments** | Within **5 days** of term start, elected stewards appoint a **Lead Steward** from among themselves; a **Secretary** may be appointed as a multisig keyholder. Role detail: [stewards & roles](stewards-and-roles.md). |

## Running the cycle

1. **Publish the nominations thread**: `[WG] Working Group Steward Nominations Term X (Year)` in the [Meta-Governance category](https://discuss.ens.domains/c/meta-governance/28). Candidates self-nominate within the nomination window. (Term 7 thread: [22157](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157).)
2. **Clear the 10,000-vote threshold**: a nominee must reach ≥10,000 supporting votes during the window to make the ballot ([rules](https://docs.ens.domains/dao/wg/rules/)).
3. **Run the ranked-choice ballot**: the election runs on [Snapshot](https://snapshot.box/#/s:ens.eth) as a ranked-choice (Copeland) vote over 120 hours; the top 3 by score are seated.
4. **Make appointments (first 5 days)**: appoint the Lead Steward (operational management, fund-disbursement initiation, DAO updates; removable by simple majority) and, optionally, a Secretary keyholder ([rules](https://docs.ens.domains/dao/wg/rules/)). See [stewards & roles](stewards-and-roles.md).
5. **Rotate multisig owners** on any seat change, per [signers.md](../04-runbook/signers.md).

Before the nomination window, Meta-Gov sets the term's compensation standards. See [funding-request.md](../04-runbook/funding-request.md).

## Term 7 (2026) timing

The steward term cycle shifted from calendar-year to a **mid-year cadence** following the "ENS Retro" restructuring, which extended Term 6 stewards and deferred elections ([nominations thread](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157)).

| Event | Date (UTC) |
| --- | --- |
| Nominations close | 22 Jun 2026 09:00 |
| Election voting (120h, ranked-choice) | 25 Jun 2026 09:00 → 30 Jun 2026 09:00 |
| Term 7 begins | 1 Jul 2026 09:00 |
| Term 7 ends | 30 Jun 2027 |

**Result.** Three seats were filled: **netto.eth**, **sovereignsignal.eth**, and **abdullahumar.eth**, with the third seat decided by the Average Support tiebreaker. Turnout 1,444,708 ENS across 60 voters, above the 1M quorum. Candidates estmcmxci.eth, jkm.eth, and vegayp.eth were not elected ([result posted 2026-07-01](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157), netto.eth). Full record: [term-07.md](../05-terms/term-07.md).

**netto.eth was appointed Lead Steward**, recorded publicly on 2026-07-13 and restated in each subsequent meeting agenda ([Term 7 meetings thread](https://discuss.ens.domains/t/meta-gov-working-group-term-7-meetings-thursday-4pm-utc-bi-weekly/22280)).

**No Secretary and no Scribe were appointed for Term 7.** The Secretary role is optional under the single-WG model ([Path forward](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)); the stewards maintain the meeting record themselves in the absence of a Scribe ([meetings thread](https://discuss.ens.domains/t/meta-gov-working-group-term-7-meetings-thursday-4pm-utc-bi-weekly/22280)).

Term 7 compensation rates (carried forward from Term 6): see [term-07.md](../05-terms/term-07.md).
