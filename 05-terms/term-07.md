# Term 7 (2026)

**Dates:** 1 Jul 2026 09:00 UTC → 30 Jun 2027 (one-year term).
**Cycle:** annual.
**Working Groups active:** **Meta-Governance only**, the sole Working Group for Term 7. The Public Goods and ENS Ecosystem WGs were dissolved per the [EP 6.44] "Metagov only" Copeland result ([winning option, 601,311 VP](https://snapshot.box/#/s:ens.eth/proposal/0xe4e1c052b2ea4f640cab27ddec326df6290d8996a9219b60cda4c4d4509f5f9a); [forum](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)).

## Stewards

Three steward seats, filled by [ranked-choice election](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157) (Copeland; voting 25–30 Jun 2026). Elected stewards, per netto.eth's result post (2026-07-01):

| Steward | Note |
|---------|------|
| netto.eth (Alex Netto) | elected |
| sovereignsignal.eth (Sov) | elected |
| abdullahumar.eth (Abdullah) | elected; third seat decided by the Average Support tiebreaker |

Turnout was 1,444,708 ENS across 60 voters, above the 1M quorum. Candidates estmcmxci.eth, jkm.eth, and vegayp.eth were not elected. Source: [Term 7 nominations and results thread](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157) (netto.eth, 2026-07-01).

**netto.eth is Lead Steward**, recorded publicly 2026-07-13 and restated in each subsequent meeting agenda ([Term 7 meetings thread](https://discuss.ens.domains/t/meta-gov-working-group-term-7-meetings-thursday-4pm-utc-bi-weekly/22280)). **No DAO Secretary and no Scribe were appointed**; the Secretary role is optional under the single-WG model and the stewards maintain the meeting record themselves.

## Funding

| WG | Proposal | Amount | Window |
|----|----------|--------|--------|
| Meta-Governance | [[Social] Funding Request: ENS Meta-Governance Working Group Term 7 (Oct. Window)](https://discuss.ens.domains/t/22475), posted 2026-10-09; **no Snapshot vote yet** (_as of 2026-10-14_, [Snapshot](https://snapshot.box/#/s:ens.eth)) | **201,559 USDC**, 0 ETH, 0 ENS | October 2026 |

The July 2026 window closed on 2026-07-31 with no Meta-Governance funding proposal. Residual Term 6 funds paid steward compensation and communications from 1 July, so no emergency request under WG Rule 10.1.2 was needed ([request](https://discuss.ens.domains/t/22475)).

The request is a Social Proposal under WG Rule 10.1.1. If it passes, the stewards submit the executable Collective Proposal in the October 2026 window. It covers **1 Oct 2026 → 30 Jun 2027** in one request, where past requests ran only to the next window ([request](https://discuss.ens.domains/t/22475)).

| Budget line (1 Oct 2026 → 30 Jun 2027) | USDC | Note |
|---|---|---|
| Steward compensation (9 months) | 121,500 | $13,500/month for three seats |
| DAO communications (9 months) | 18,540 | $2,060/month → [monthly-compensation](../04-runbook/monthly-compensation.md) |
| Discretionary (governance and community) | 50,000 | Ceiling; travel and contributor costs; no grants or programs |
| Contract audits (conditional) | 100,000 | Ceiling; released only for DAO-approved audits, first expected Governor Nexus; unused returns to the treasury |
| **Total** | **290,040** | |
| Less USDC held on 2026-10-07 | −88,481 | |
| **Requested** | **201,559** | |

Source: [request](https://discuss.ens.domains/t/22475). No ETH or ENS is requested: the steward ENS component comes from ENS already in the Safe (see Compensation). The stewards will report spending against this budget at the April 2027 window and at term end.

**Rules 11.2 / 11.3.** The request states that the executable will detail Term 7 steward compensation, **ratify** compensation paid from residual Term 6 funds from 1 July 2026 until execution, and **authorize** it from execution to 30 June 2027 ([request](https://discuss.ens.domains/t/22475)).

> ⚠️ **Open question:** The Snapshot result, the EP number, and the executable are pending → [OPEN-QUESTIONS Q-05](../OPEN-QUESTIONS.md).

## Compensation

No standalone "Term 7 Compensation" proposal exists. Rates are codified within **[EP 6.44 [Social] Path forward on Working Groups for Term 7](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)** ([Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xe4e1c052b2ea4f640cab27ddec326df6290d8996a9219b60cda4c4d4509f5f9a)), carried forward unchanged from Term 6, as stated by netto.eth (#4/#9):

| Role | Rate (as stated) |
|------|------------------|
| Lead Steward | $5.5k/month + ENS* |
| Steward | $4k/month + ENS* |
| Secretary | $5.5k/month — **role not filled in Term 7** |
| Scribe | $3k/month — **role not filled in Term 7** |

\* 2-year vested ENS, calculated using the 6-month TWAP, distributed mid-term, matching the USD value of the salaries. The funding request sizes the Term 7 ENS component at **$162,000** (twelve months of USDC compensation), paid from the 45,129 unencumbered ENS already in the Safe. That covers it at any six-month TWAP of $3.59 or more; below that, the stewards will request the shortfall in the next window ([request](https://discuss.ens.domains/t/22475)).

Under the winning "Metagov only" option, Secretary and Scribe are **not** ballot-mandated: per Coltron.eth (#10) and 184.eth (#6), Secretary is a steward nomination per WG Rules and Scribe is funded at the elected stewards' discretion.

## Multisig

| WG | Safe | Threshold |
|----|------|-----------|
| Meta-Governance (`main.mg.wg.ens.eth`) | [see addresses.md](../02-contracts-and-multisigs/addresses.md) | 2 of 4 |

The Term 7 signer rotation is **executed**. The Safe is **2 of 4**: the three elected stewards plus the DAO Timelock (`wallet.ensdao.eth`) in place of the former Secretary seat. Confirmed via the [Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/) and a direct `getThreshold()` / `getOwners()` call on 2026-08-19 (nonce 243). Roster in [addresses.md](../02-contracts-and-multisigs/addresses.md); rationale in [multisigs.md](../02-contracts-and-multisigs/multisigs.md).

Note the outcome differs from the 2-of-3 anticipated in the ["Path forward"](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) thread.

## Activity

- **Term 7 funding request posted** 2026-10-09: 201,559 USDC for 1 Oct 2026 → 30 Jun 2027; Snapshot vote not yet open (_as of 2026-10-14_). See [Funding](#funding) and the [request](https://discuss.ens.domains/t/22475).
- **Delegation Incentives Program pilot ended**: Rounds 1–3 paid 18,000 ENS from the Meta-Gov Safe; Round 3 closed 2026-09-30. EP 6.47 (forum numbering) provides that the remaining **72,000 ENS is returned to the treasury** once the pilot concludes ([request](https://discuss.ens.domains/t/22475); [EP 6.47 thread](https://discuss.ens.domains/t/6-47-executable-delegation-incentives-program-funding-transfer/22228)). **Not yet returned**: the Safe still held 117,129 ENS on 2026-10-14 ([Safe API balances](https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/balances/)).
- **Term 7 steward election concluded** (25–30 Jun 2026, ranked-choice Copeland): netto.eth, sovereignsignal.eth, and abdullahumar.eth elected; result posted [2026-07-01 in thread 22157](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157).
- **Meta-Gov Safe rotated to the Term 7 signers** on 2026-07-30 (2-of-4: three steward keys + the Timelock; [tx](https://etherscan.io/tx/0xd646d8f1171eb33a23d8259eb237c173b13b8eb8c2060ff0860e4c21745985f1)). See [multisigs.md](../02-contracts-and-multisigs/multisigs.md).
- **SafeNotes shut down** (announced [2026-09-01](https://discuss.ens.domains/t/safenotes-shutting-down/22398), citing Meta-Governance not continuing to support it); the annotated WG transaction record 2022–2026 is archived → [wg-transaction-history.md](../reference/wg-transaction-history.md). Replacement practice undecided → [Q-30](../OPEN-QUESTIONS.md).
- [**EP 6.44 [Social] Path forward on Working Groups for Term 7**](https://snapshot.box/#/s:ens.eth/proposal/0xe4e1c052b2ea4f640cab27ddec326df6290d8996a9219b60cda4c4d4509f5f9a): Copeland ranked-choice vote; "Metagov only" won (Meta-Gov sole WG; Public Goods + Ecosystem dissolved). Carried the Term 7 election fallback timeline and compensation guidelines. Closed ~1 Jun 2026.
- [**Meta-Governance Working Group Steward Nominations Term 7 (2026)**](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157): nomination window 2–22 Jun 2026 09:00 UTC; election 25–30 Jun 2026 (120h, ranked-choice Copeland); 3 steward seats.
- [**Path forward on Working Groups for Term 7 (forum discussion)**](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107): restructure rationale, timeline, comp structure, WG Rule amendments (posted 12 May 2026).
- [**[Temp Check] Metagov Update: Working Group Operations During the ENS Retro**](https://discuss.ens.domains/t/temp-check-metagov-update-working-group-operations-during-the-ens-retro/21781): context for delayed elections / reduced-capacity WG operations leading into Term 7.
- [**EP 6.25 [Social] Replace the Working Groups with the ENS Admin Panel**](https://snapshot.box/#/s:ens.eth/proposal/0xbc44d9714ee818da49c25998cabdbe745f939fef74923255c3571a00e8977e5d): earlier restructure temp check (Against won). Closed ~3 Dec 2025.
