# Critical Proposals: Annotated Timeline

This is a curated timeline of the proposals that **changed the rules, governance structure, or core processes** of the ENS DAO, not an exhaustive catalog. For the full archive, see the [ENS Docs proposals index](https://ens.gov.blockful.io/proposals) and the [Governor proposal mirror](https://dao.ens.gregskril.com/). Addresses cited below live in the canonical [addresses table](../02-contracts-and-multisigs/addresses.md).

> **EP numbering:** the leading digit is the term number (`EPN.M` = proposal *M* of Term *N*); older proposals were renumbered from a legacy `EP1–EP16` scheme. See [proposal numbering](../01-governance/proposals.md).

## Founding & Constitution

| EP / Date | What changed | Source |
|---|---|---|
| **Constitution ratified** · 2021-11-15 | Ratified the 5-article Constitution (name-ownership, fees-as-incentive, treasury allocation, DNS integration, amendment rule). Amendable only by 2/3 supermajority + 1% quorum. 97% approval. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xd810c4cf2f09737a6f833f1ec51eaa5504cbc0afeeb883a21a7e1c91c8a597e4) |
| **EP0.1** · 2021-11-24 | Transferred the treasury and core contract ownership from the legacy `multisig.ens.eth` to the DAO timelock, the foundation of today's contract hierarchy. | [Docs](https://docs.ens.domains/dao/proposals/0.1/) |

## Working-Group structure (EP0.4 → EP1.8 → EP4.8 → EP6.44)

The proposals that reshaped the [WG Rules](https://docs.ens.domains/dao/wg/rules/). For the full structural-evolution narrative (4 WGs → Meta-Gov-only), see [../05-terms/README.md](../05-terms/README.md).

| EP / Date | What changed | Source |
|---|---|---|
| **EP0.4** · 2021-12-16 | Created the WG system: **four** WGs (Meta-Gov, ENS Ecosystem, Community, Public Goods), **five** stewards each, two 6-month terms/year. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x899ead1d9b9b98f63f6a60dc0939bef55dbe365e78c6a550f07be969a47f148b) |
| **EP1.8 / EP12** · 2022-06-05 | Rewrote the WG charter: reduced to **three** stewards/group, introduced Lead Stewards and the DAO Secretary, funding windows (Jan/Apr/Jul/Oct), and 3-of-4 multisig signing. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xc7186cf8bebe47600f8d847e76f7971ea97b48bc04eda1e07780aff91fb6410d) |
| **EP4.8** · 2023-11-03 | Merged the two 6-month terms into one **annual** calendar term; made Meta-Gov responsible for defining compensation standards before each nomination window. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x26a5c8dec547837495707e70446d1e7cd874a91f75753c602998f6e70083a266) |
| **EP6.44** · 2025-05-27 | "Path forward on Working Groups for Term 7": Copeland vote, **"Metagov only" won**: dissolved Public Goods and Ecosystem, leaving Meta-Gov the sole operational WG. Affirmed a 2/3 intra-group steward-removal safeguard. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xe4e1c052b2ea4f640cab27ddec326df6290d8996a9219b60cda4c4d4509f5f9a) |

> ⚠️ **Open question:** the Community WG was dissolved by temp check (29 May 2022, effective end of First Term 2022), but the executed dissolution EP page was not located.

## Endowment & treasury policy

| EP / Date | What changed | Source |
|---|---|---|
| **EP2.2.5** · 2022-11-23 | Selected **karpatkey** (over Avantgarde, Llama) as Endowment fund manager via ranked-choice; established the manager relationship and fee model. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x1ab7ef84f6e904582d5b5b921944b5b1a8e36dbff1f1248fde87fef02b046816) |
| **EP3.4** · 2023-02-26 | Funded the Endowment's first tranche (16,000 ETH per docs), standing up the karpatkey-managed reserve and its Roles-Modifier permission framework. | [Docs](https://docs.ens.domains/dao/proposals/3.4/) |
| **EP4.5** · 2023-11-03 | Established the DAO-voted permissions policy via the **Zodiac Roles Modifier** (Avatar/Manager Safe model): karpatkey may execute only pre-approved DeFi actions. | [Docs](https://docs.ens.domains/dao/proposals/4.5/) |
| **EP5.12** · 2024-07-02 | Migrated endowment permissions to **Roles Modifier V2**: spending limits, logical conditions, updated protocol allowlist. Base layer for all later "Update #N" proposals. | [Docs](https://docs.ens.domains/dao/proposals/5.12/) |
| **EP5.20** · 2024-10-24 | Ratified the **Investment Policy Statement**: target ~60% ETH / 40% stablecoins, monthly transfer of 33% of net income to the Endowment, biweekly rebalancing, annual IPS review. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x085a1e40c264ffd44567b6dce889f5943e72cfa8442eaeb81819261a38f0bd0a) |
| **EP6.39** · 2026 | Treasury Flow Automation: timelock maintains a **6-month USDC runway** (~$8M), recalculated quarterly by karpatkey. | [Forum](https://discuss.ens.domains/t/executable-treasury-flow-automation/21923) |

> ⚠️ **Open question:** EP6.39's separate *endowment-level* multi-year stablecoin runway was reported inconsistently ("two-year" vs "three-year"); the 6-month timelock figure is verified.

See also [../03-treasury-and-endowment/](../03-treasury-and-endowment/) for the funding-tranche history (EP3.4 / EP4.2 / EP6.2) and the Update #N permission series.

## Security Council

| EP / Date | What changed | Source |
|---|---|---|
| **EP5.7** · 2024-05-04 | Established the original Security Council concept: a multisig with the cancel role on the timelock to veto malicious proposals; framed as a ~2-year measure. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xf3a4673fe04a3ecfed4a2f066f6ced1539a5466d61630428333360b843653c54) |
| **EP5.10** · 2024-06-24 | Confirmed the Council's specific membership, operationalizing the cancel/veto safeguard. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xa0b1bfadf6853b5b0d59d3c4d73c434fc6389339887d05de805361372eb17c3a) |
| **EP5.13** · 2024 (executed ~28 Jul) | Deployed `SecurityCouncil.sol` and granted it PROPOSER_ROLE on the timelock so the 4-of-8 council can **cancel (veto)** queued operations. Cancel-only by design; 2-year auto-expiry (24 Jul 2026). | [Docs](https://docs.ens.domains/dao/proposals/5.13/) |
| **2026 renewal** · temp check | A new, Nethermind-audited (NM-0945) `SecurityCouncil` contract adds an `extend()` function so future renewals are a single governance vote; re-grants PROPOSER_ROLE before the 2024 council expires. | [Temp check](https://discuss.ens.domains/t/temp-check-renewal-of-the-security-council/22145) |

> ⚠️ **Open question:** as of 2026-06-20 the renewal was still at temp-check stage. No Snapshot/EP number or deployed mainnet address had been assigned.

## Service Provider Program

| EP / Date | What changed | Source |
|---|---|---|
| **SPP1 founding** · 2023-11-07 | Founded the Service Provider Program: **$3.6M/year** continuous streams to full-time ENS teams, selected by approval voting; streams cancellable by the DAO. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x5748982aed143f51333befbc6cc490116648b85a2b0212fdfaf3ab848932c7ae) |
| **EP5.2** · 2024-01-18 | Commenced SPP1 streams via **Superfluid** and a Stream Management Pod Safe, the standing streaming mechanism reused for SPP2. | [Docs](https://docs.ens.domains/dao/proposals/5.2/) |
| **EP6.3** · 2025-02-25 | Renewed the program for **Season 2 at $4.5M/year**; set two-year vs one-year allocation tranches, application deadline, quarterly KPIs, Meta-Gov oversight. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x0cca1cf36731203e235b0e2de9041be3a16d9cdeadff6e15e1f1215c611e12ef) |
| **EP6.10** · 2025-05-08 | Selected the SPP2 cohort (~8 providers) via Copeland ranked-choice against a "NONE BELOW" baseline. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0x98c65ac02f738ddb430fcd723ea5852a45168550b3daf20f75d5d508ecf28aa1) |
| **EP6.13** · 2025-06-26 | Implemented SPP2: routes $4.5M/yr USDC from the timelock through the Stream Management Pod via Superfluid to the 8 providers. (Corrected version; first attempt failed at NO_QUORUM.) | [Proposal](https://dao.ens.gregskril.com/proposal/20404686300257550242704646761273386459664655640264490428281621095220078268383) |

## Registry / Root control

| EP / Date | What changed | Source |
|---|---|---|
| **EP3.5** · 2023-03-29 | Activated a new `.eth` ETHRegistrarController, NameWrapper-as-controller, and a new ReverseRegistrar: core registrar/controller infrastructure change. | [Docs](https://docs.ens.domains/dao/proposals/3.5/) |
| **EP4.10** · 2023 | Transferred ENS **root key ownership** from the legacy 7-keyholder multisig to the DAO. | [Docs](https://docs.ens.domains/dao/proposals/4.10/) |
| **EP5.27** · 2024-12-11 | Permanently **revoked the DAO's own power** to set the NameWrapper upgrade contract, a self-limiting act removing a seizure vector over user names. | [Docs](https://docs.ens.domains/dao/proposals/5.27/) |
| **EP6.7** · 2025-04-24 | Revoked the legacy ENS multisig's **root-controller** role (create/replace non-`.eth` TLDs), consolidating root/TLD admin under the DAO. | [Forum](https://discuss.ens.domains/t/ep-6-8-executable-revoke-root-controller-role-from-legacy-ens-multisig/20644) |

> ⚠️ **Open question:** anticapture shows two "EP6.7"-titled items on the same date; the forum thread references EP6.8. The canonical number for the root-controller revocation is unconfirmed.

## Governance distribution

| EP / Date | What changed | Source |
|---|---|---|
| **EP5.19** · 2024-10-23 | Approved the **Governance Distribution Pilot** (30,000 ENS), a delegation/participation incentive to improve delegate engagement and decentralize voting power. | [Snapshot](https://snapshot.box/#/s:ens.eth/proposal/0xfa54ff2b55f0495c96ec2d8645241bcff48ca6afe1f4925fb51f29c4667252df) |
| **EP5.26** · 2024-11-20 | Implemented EP5.19: transferred 30,000 ENS to the Meta-Gov wallet for distribution via 2-year linear vesting to DAO contributors. | [Proposal](https://dao.ens.gregskril.com/proposal/50152158826647742094695349340830523178083147237337111134725087674188893435887) |
