# Changelog

Notable revisions to the runbook itself. For terminology see [`glossary.md`](glossary.md); for the DAO's structural / working-group evolution (4 WGs → Meta-Gov-only), see [`../05-terms/README.md`](../05-terms/README.md).

Per [`../CONTRIBUTING.md`](../CONTRIBUTING.md), re-verify stewards, compensation, and multisig thresholds each new term, and re-verify addresses on any contract change.

## Document revisions

| Date | Revision |
| --- | --- |
| _as of 2026-06-20_ | Initial runbook drafted; Term 7 transition (Meta-Gov sole WG) reflected as current. |
| _2026-07-11_ | Recorded the Term 7 steward election result (netto.eth, sovereignsignal.eth, abdullahumar.eth) and both Term 6 steward ENS distribution tranches (2025-08-06 and 2026-07-11, via Hedgey); narrowed Q-01, updated Q-03 (Safe still 3/4). |
| _2026-07-11_ | Closed Q-26: the [Term 6 Dashboard](https://discuss.ens.domains/t/ens-dao-term-6-dashboard/20076) mislinked netto.eth's forum handle to estmcmxci's profile; corrected by estmcmxci (steward-confirmed) — netto.eth and estmcmxci are distinct people, Meta-Gov seat belongs to netto.eth as already recorded in [05-terms/term-06.md](../05-terms/term-06.md). |
| _2026-07-28_ | Recorded the 2026 Security Council renewal: EP6.48 (Renewal Term 2) defeated 2026-07-05, then "Establishing a new Security Council" executed 2026-07-22 (new contract 0x2acBf5…, new 5/8 Safe 0x7101B7…, PROPOSER_ROLE granted before the 2024 veto expired 2026-07-24). Updated security-council.md, addresses.md, governance-history.md, calendar.md; resolved Q-09, updated Q-10. |
| _2026-08-20_ | Term 7 currency pass. Closed Q-01 (Lead Steward netto.eth, public 2026-07-13), Q-02 (no Secretary appointed) and Q-04 (`EP7.x` confirmed in use via `[7.1]`); restated Q-05 for the missed July window and the Rule 11.2/11.3 question. Recorded that **no Scribe was appointed** for Term 7 and marked both unfilled roles in the compensation table. Resolved the stale Security Council temp-check note in `governance-history.md`. Added the monthly delegate all-hands and the recorded-call/summary commitment to `calendar.md`. Fixed `elections.md`, which still described the election as undecided. Added `scripts/check_currency.py` and a scheduled workflow to test stated Safe thresholds against the chain. |
| _2026-08-19_ | Corrected the Meta-Gov Safe config: rotation executed, threshold **3/4 → 2/4**, owners are the three elected stewards plus the DAO Timelock in place of the Secretary seat (verified on-chain, nonce 243). Added the signer roster to addresses.md. Corrected the MetaGov call cadence to Thursdays 16:00 UTC bi-weekly (thread 22280); the Tuesdays-9am-ET slot was Term 6. Resolved Q-03 and the matching open questions in stewards-and-roles.md and signers.md. |
