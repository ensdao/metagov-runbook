# Directory — Who's Who

Public identities only (ENS / forum handles). Addresses live in [02-contracts-and-multisigs/addresses.md](02-contracts-and-multisigs/addresses.md). Cadence in [04-runbook/calendar.md](04-runbook/calendar.md); links in [reference/resources.md](reference/resources.md). _Roster as of 2026-06-20._

## Working Groups & forum categories

| WG | Forum category (id) | Status |
|---|---|---|
| Meta-Governance (`main.mg.wg.ens.eth`) | Meta-Governance (28) | **Sole operational WG** for Term 7 — governance oversight + DAO/WG operations ([Path forward](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)) |
| ENS Ecosystem (`main.eco.wg.ens.eth`) | ENS Ecosystem (32) | **Legacy** — dissolved for Term 7; unspent funds return to treasury ([Path forward](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)) |
| Public Goods (`main.pg.wg.ens.eth`) | Public Goods (37) | **Legacy** — dissolved for Term 7 |

## Roles

| Role | Holder(s) | Notes |
|---|---|---|
| Meta-Gov Stewards (Term 6 / 2025, current docs roster) | 5pence.eth, netto.eth, daostrat.eth | Most recent confirmed roster ([stewards](https://docs.ens.domains/dao/stewards/)) |
| Lead Steward | one per WG; appointed within 5 days of term start | Operational management, fund-disbursement initiation, DAO updates ([WG Rules](https://docs.ens.domains/dao/wg/rules/)) |
| DAO Secretary | appointed by majority of all stewards | 4th multisig keyholder; cross-WG coordination; paid by Meta-Gov. Optional in Term 7 ([WG Rules](https://docs.ens.domains/dao/wg/rules/)) |
| Security Council (4-of-8) | 8 members — roster and expiry in [security-council.md](02-contracts-and-multisigs/security-council.md) | Cancel/veto-only mandate; members confirmed [EP5.10](https://docs.ens.domains/dao/proposals/5.10/) |

> ⚠️ **Open question:** Final Term 7 Meta-Gov stewards, Lead Steward, and whether a Secretary is appointed are undecided (election 25–30 Jun 2026). Nominees: estmcmxci.eth, jkm.eth, sovereignsignal.eth, vegayp.eth ([thread 22157](https://discuss.ens.domains/t/meta-governance-working-group-steward-nominations-term-7-2026/22157)).

## Service providers

| Team | Role | SPP2 stream |
|---|---|---|
| [karpatkey](https://reports.kpk.io/ens) (kpk) | Endowment manager since Mar 2023; non-custodial on-chain management; weekly ops reports + MetaGov presentations | — |
| [Steakhouse Financial](https://discuss.ens.domains/t/ens-financial-reporting-by-steakhouse/16601) | Treasury/endowment financial reporting (joint endowment proposal with karpatkey) | — |
| [NameHash Labs](https://discuss.ens.domains/t/spp2-namehash-labs-application/20502) | ENS infra/tooling (ENSNode, ENSRainbow, NameGuard) | $1.1M/yr |
| [blockful](https://discuss.ens.domains/t/blockful-service-provider-reports/19553) | Governance security: continuous calldata review, Anticapture, security-council contract | $700k/yr |
| [ETH.LIMO](https://discuss.ens.domains/t/spp2-eth-limo-application/20369) | Public ENS gateway / default resolver | $700k/yr |
| [Ethereum Identity Foundation](https://discuss.ens.domains/t/spp2-ethereum-identity-foundation-application/20439) | Ethereum Identity Kit, Ethereum Follow Protocol | $500k/yr |
| [Unruggable](https://discuss.ens.domains/t/spp2-unruggable-application/20485) | Unruggable Gateways, L2 resolution, ENSv2 | $400k/yr |
| [Namespace](https://discuss.ens.domains/t/spp2-namespace-application/20456) | ENS subname adoption tools/partnerships | $400k/yr |
| [ZK Email](https://discuss.ens.domains/t/spp2-zk-email-application/20450) | ZK proofs over email; Email-as-ENS _(new in S2)_ | $400k/yr |
| [JustaName](https://docs.justaname.id) | ENS SDK/toolkit, off-chain subnames, SIWENS _(new in S2)_ | $300k/yr |

Provider allocations per [EP6.13](https://docs.ens.domains/dao/proposals/6.13/).

## Core development & audits

| Entity | Role |
|---|---|
| **ENS Labs / True Names Ltd** | Core protocol software development; separate legal entity from the DAO, led by Nick Johnson (nick.eth). Forum: ENS Development (42) ([core-team transitions](https://discuss.ens.domains/t/core-team-transitions/17726)) |
| **blockful** | Confirmed ENS governance-security author (Anticapture framework, calldata review) ([assessment](https://discuss.ens.domains/t/governance-security-assessment/21898)) |
| **Nethermind** | Audited the renewed SecurityCouncil contract — review NM-0945, zero findings ([repo](https://github.com/blockful/security-council-ens)) |
| **Cyfrin** | Audited the EP6.39 Treasury Flow Automation contracts ([thread 21923](https://discuss.ens.domains/t/executable-treasury-flow-automation/21923)) |
| **Ackee** (and Sub 7) | Audited the endowment Zodiac Roles Modifier ([EP3.4](https://docs.ens.domains/dao/proposals/3.4/)) |

> ⚠️ **Open question:** Nethermind, Cyfrin, and Ackee are cited from specific proposal/repo sources above, but a single canonical ENS index tying these firms to ENS-governance audits was not found ([directory note](https://discuss.ens.domains/t/governance-security-assessment/21898)).

## Escalation / how to reach

| Need | How to reach | Notes |
|---|---|---|
| **A malicious proposal is queued and could execute** | Trigger the **Security Council** — the 4-of-8 council Safe vetoes (cancels) the queued Timelock operation inside its delay window. Procedure and roster: [security-council.md](02-contracts-and-multisigs/security-council.md) | Any delegate can alert the council; post the alert to the Meta-Governance category ([28](https://discuss.ens.domains/c/meta-governance/28)) so signers convene fast |
| **Reach the Meta-Gov stewards** | Meta-Governance forum category ([28](https://discuss.ens.domains/c/meta-governance/28)); weekly public MetaGov call (Tuesdays 9am ET); Meta-Gov Stewards forum group | All channels indexed in [reference/resources.md](reference/resources.md) |
| **Suspected phishing / address-poisoning at signing** | Stop and follow [04-runbook/verification-and-safety.md](04-runbook/verification-and-safety.md); do not sign until verified | Log unverified payouts to [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |

## Tooling & links

All voting front-ends, dashboards, and canonical URLs are consolidated in [reference/resources.md](reference/resources.md).
