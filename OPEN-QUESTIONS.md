# Open Questions

Items that **could not be verified** from a primary source, or that are **in motion** as of 2026-06-20. Per the project's no-assumptions rule, none of these is asserted as fact anywhere in the docs. They're collected here for the stewards to resolve. Each has a stable ID, the source that surfaced it, and (where known) the files that would carry the answer. Resolve → add the cited fact to the owner file and remove the entry.

## Live / time-sensitive (Term 7 transition)

- **Q-01: Term 7 Lead Steward and Secretary.** The three Meta-Gov stewards were elected (netto.eth, sovereignsignal.eth, abdullahumar.eth; [result 2026-07-01](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157)), now recorded in [05-terms/term-07.md](05-terms/term-07.md). Still open: the Lead Steward and whether a Secretary is appointed (see Q-02) were not yet named as of 2026-07-11.
  _Refs: [01-governance/elections.md](01-governance/elections.md), [directory.md](directory.md), [05-terms/term-07.md](05-terms/term-07.md)._
- **Q-02: Secretary under the single-WG model.** Is a Secretary still appointed now that Meta-Gov is the sole WG? The "Path forward" vote makes it optional/at stewards' discretion. ([22107](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107))
  _Refs: [01-governance/stewards-and-roles.md](01-governance/stewards-and-roles.md), [05-terms/README.md](05-terms/README.md)._
- **Q-03: Meta-Gov multisig 3/4 → 2/3.** The Path-forward thread indicates a move toward 2-of-3 signing with the Secretary seat optional. As of 2026-07-11 the Safe is **still 3 of 4 with the Term 6 owners** (nonce 235); the Term 7 signer rotation is pending. Re-verify on-chain once it happens.
  _Refs: [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md), [02-contracts-and-multisigs/multisigs.md](02-contracts-and-multisigs/multisigs.md)._
- **Q-04: Term 7 EP prefix.** Is it `EP7.x`? The leading-digit-=-term scheme is explicitly confirmed only for Terms 3–4; no EP7.x proposal exists yet.
  _Refs: [01-governance/proposals.md](01-governance/proposals.md)._
- **Q-05: Term 7 Meta-Gov funding.** The Collective funding-request EP id and amount are not yet posted (funding window opens after 1 Jul 2026).
  _Refs: [05-terms/term-07.md](05-terms/term-07.md), [04-runbook/funding-request.md](04-runbook/funding-request.md)._
- **Q-06: Funding-window cadence under the July anchor.** Whether the historical Jan/Apr/Jul/Oct windows shift with the new July–June cycle is not documented.
  _Refs: [04-runbook/calendar.md](04-runbook/calendar.md), [04-runbook/funding-request.md](04-runbook/funding-request.md)._
- **Q-07: Term anchor after Term 7.** Whether Term 8+ reverts to a Jan-1 anchor or stays July-anchored (a consequence of the Retro 6-month shift) is unresolved.
  _Refs: [05-terms/README.md](05-terms/README.md), [04-runbook/calendar.md](04-runbook/calendar.md)._
- **Q-08: Single-WG formalization.** Were the Constitution / WG Rules pages formally amended for the single-WG structure, or does it stand solely on the Snapshot outcome?
  _Refs: [01-governance/constitution.md](01-governance/constitution.md), [05-terms/README.md](05-terms/README.md)._

## Security Council

- **Q-09: 2026 renewal status.** As of 2026-06-20 the Nethermind-audited renewal is at **temp-check only** ([22145](https://discuss.ens.domains/t/temp-check-renewal-of-the-security-council/22145)). No EP number, no deployed contract address, no `grantRole(PROPOSER_ROLE,…)` tx. The 2024 council's veto expires **2026-07-24**, so the renewal must land before then.
  _Refs: [02-contracts-and-multisigs/security-council.md](02-contracts-and-multisigs/security-council.md), [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md)._
- **Q-10: Council Safe ↔ member mapping.** EP 5.10 names 8 members; confirm the on-chain 4/8 Safe (`0xaA5cD0…2Cc7`) owners match those identities and threshold = 4.
  _Refs: [02-contracts-and-multisigs/security-council.md](02-contracts-and-multisigs/security-council.md), [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md), [directory.md](directory.md)._

## Contracts & addresses

- **Q-11: ENS Root owner identity.** `root.ens.eth` owner resolves to `0x4Fe4e666…e3e0e8`, which is **not** the Timelock (`0xFe89…44b7`). Is it the Timelock proper, a dedicated DAO root multisig, or a wrapper? The exact DAO→root chain of control needs confirmation.
  _Refs: [02-contracts-and-multisigs/ens-protocol-control.md](02-contracts-and-multisigs/ens-protocol-control.md), [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md)._
- **Q-12: `controller.ens.eth` alias lag.** The alias resolves to the older `0x2535…303b` while the deployments wiki lists `0x59E1…eA547` as the active ETHRegistrarController. Intentional or just not updated?
  _Refs: [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md), [02-contracts-and-multisigs/ens-protocol-control.md](02-contracts-and-multisigs/ens-protocol-control.md)._
- **Q-13: Current Roles Modifier V2 instance.** Is `0x703806…0A40` still the sole/current Zodiac Roles instance, or superseded by an "Update #N" beyond EP 6.38?
  _Refs: [03-treasury-and-endowment/endowment-permissions.md](03-treasury-and-endowment/endowment-permissions.md), [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md)._

## Treasury & endowment

- **Q-14: Endowment-level runway horizon.** EP 6.39 confirms a **6-month USDC runway at the Timelock**, but the longer endowment-level stablecoin runway was reported inconsistently as 2-year vs 3-year. Pin the exact figure from the canonical proposal text.
  _Refs: [03-treasury-and-endowment/treasury-automation.md](03-treasury-and-endowment/treasury-automation.md), [03-treasury-and-endowment/endowment.md](03-treasury-and-endowment/endowment.md)._
- **Q-15: Performance-fee settlement.** The on-chain settlement pattern for karpatkey's 10% performance fee is unverified (only the monthly Endowment Reports document it). How/where is it settled?
  _Refs: [04-runbook/treasury-manager-fees.md](04-runbook/treasury-manager-fees.md), [03-treasury-and-endowment/endowment.md](03-treasury-and-endowment/endowment.md)._
- **Q-16: Unverified Meta-Gov Safe payouts.** Tie to a governing EP, or flag as phishing: 75,000 USDC to `0x149b9013…4dec` (2026-05-01); recurring 18,000 USDC to `0x8320ea…718df` (2026-04-15, 2026-05-08). **The second recipient matches a known address-poisoning lookalike**. Confirm whether these are legitimate payments or phishing artifacts.
  _Refs: [04-runbook/verification-and-safety.md](04-runbook/verification-and-safety.md), [04-runbook/monthly-compensation.md](04-runbook/monthly-compensation.md)._
- **Q-17: SPP2 stream details & pod membership.** Current per-provider stream rates / remaining durations (basic vs extended scopes), stream on/off-boarding handling, and the exact Stream Management Pod signers are unconfirmed.
  _Refs: [03-treasury-and-endowment/service-provider-program.md](03-treasury-and-endowment/service-provider-program.md), [directory.md](directory.md)._

## Directory & audits

- **Q-18: Auditor attribution.** Nethermind, Cyfrin, and Ackee are each cited from a specific source, but no single canonical ENS index ties these firms to ENS-governance audits. `blockful` is confirmed for governance security / calldata review.
  _Refs: [directory.md](directory.md)._

## Per-term archive gaps (05-terms/)

- **Q-19: EP numbering discrepancies.** EP 6.44 ("Path forward") is dated 2025-05-27 in one facet and 2026-05-27 in others. Reconcile. Anticapture shows two "EP 6.7"-titled items same-day (transfer .ceo TLD vs revoke root controller); the forum references EP 6.8. Confirm the canonical number.
  _Refs: [01-governance/proposals.md](01-governance/proposals.md), [reference/governance-history.md](reference/governance-history.md)._
- **Q-20: Community WG dissolution EP.** Dissolved by temp check (29 May 2022, effective end of First Term 2022); the executed dissolution EP page was not located.
  _Refs: [05-terms/term-01.md](05-terms/term-01.md), [reference/governance-history.md](reference/governance-history.md)._
- **Q-21: Per-role compensation rates, Terms 2–3.** Term 2 (Q3/Q4 2022) per-role monthly rates live only in budget-table **images** (not machine-readable); Term 3 states only aggregates. Open the images / proposal bodies to confirm exact figures before publishing rate tables.
  _Refs: [05-terms/term-02.md](05-terms/term-02.md), [05-terms/term-03.md](05-terms/term-03.md)._
- **Q-22: Term 4 Lead Steward 6-month figure.** Source states $13,500 for a 6-month lead term, inconsistent with the stated $4,500/mo. Reported as-stated; confirm against the raw post.
  _Refs: [05-terms/term-04.md](05-terms/term-04.md)._
- **Q-23: Term 6 compensation proposal EP id.** A forum read labeled it "EP 5.18" but that isn't in the docs proposals index; confirm the canonical id and the rate table ($588k total) line-by-line.
  _Refs: [05-terms/term-06.md](05-terms/term-06.md)._
- **Q-24: Historical WG Safe configs.** WG Safe addresses/thresholds for Ecosystem & Public Goods in Terms 1–4, and the Meta-Gov Safe's per-term owner set/threshold, reflect *current* state only. Historical configs are unverified.
  _Refs: [02-contracts-and-multisigs/multisigs.md](02-contracts-and-multisigs/multisigs.md), [05-terms/README.md](05-terms/README.md)._
- **Q-25: Scribe holders.** The Scribe role is funded from Term 4 onward but the person holding it in Terms 4–7 was not identified.
  _Refs: [01-governance/stewards-and-roles.md](01-governance/stewards-and-roles.md), [05-terms/README.md](05-terms/README.md)._
- **Q-26: netto.eth vs estmcmxci handle.** The Term 6 Dashboard lists netto.eth's forum handle as "estmcmxci" (Marcus/estmcmxci.eth), likely a dashboard artifact; confirm they are distinct people and the Meta-Gov seat belongs to netto.eth.
  _Refs: [05-terms/term-06.md](05-terms/term-06.md), [directory.md](directory.md)._
- **Q-27: Term 2 combined funding executable.** On-chain IDs / Tally links for the combined Term 2 collective funding executable (EP16.1/16.2/16.3 → docs EP2.2.x) not retrieved.
  _Refs: [05-terms/term-02.md](05-terms/term-02.md), [reference/governance-history.md](reference/governance-history.md)._

---

*Every item above is unverified or in motion; none is asserted as fact elsewhere in these docs. Adding a fact to the docs without a primary source is prohibited. Resolve an item here with a citation, move the cited fact to its owner file, then delete the entry.*
