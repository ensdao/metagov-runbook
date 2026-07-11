# Glossary

Concise definitions of ENS DAO and Meta-Governance terms. Addresses live in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

| Term | Definition |
| --- | --- |
| **Working Group (WG)** | A DAO unit run by elected stewards. As of Term 7, [Meta-Governance is the sole WG](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107); Ecosystem and Public Goods were dissolved. |
| **Steward** | An elected member who runs a WG, chosen by [self-nomination then ranked-choice (Copeland)](../01-governance/elections.md) election ([WG Rules](https://docs.ens.domains/dao/wg/rules/)). |
| **Lead Steward** | One steward per WG, appointed from among the elected stewards within 5 days of term start. Represents the WG, initiates fund disbursement, and reports WG spending ([WG Rules](https://docs.ens.domains/dao/wg/rules/)). |
| **Secretary (DAO Secretary)** | Optional role appointed by majority vote of all stewards; when present, acts as an additional multisig keyholder and handles cross-WG coordination. Introduced by [EP1.8](https://docs.ens.domains/dao/proposals/1.8/); [Term 7 stewards may opt not to appoint one](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107). |
| **Scribe** | A supporting compensated role in earlier terms' compensation tables (alongside steward/lead/secretary) ([comp post, Nov 2023](https://discuss.ens.domains/t/q3-q4-2023-ens-dao-dashboard/17431)). |
| **EP (Executable Proposal number)** | A proposal's identifier in the [docs archive](https://docs.ens.domains/dao/proposals/); the leading digit is the term number (EP6.x = Term 6). See [proposal numbering](../01-governance/proposals.md). |
| **Social proposal** | Off-chain proposal decided on [Snapshot](https://snapshot.org/#/ens.eth). Thresholds in [proposal types](../01-governance/proposals.md) ([process](https://docs.ens.domains/dao/governance/process/)). |
| **Executable proposal** | On-chain proposal run through the [Governor](https://www.tally.xyz/gov/ens) and Timelock. Proposal/quorum/approval thresholds and the timelock delay live in [proposal types](../01-governance/proposals.md) ([process](https://docs.ens.domains/dao/governance/process/)). |
| **Constitutional proposal** | A special social proposal (with a diff) amending the [Constitution](https://docs.ens.domains/dao/constitution/); keeps normal quorum but requires a **two-thirds** supermajority ([thresholds](../01-governance/proposals.md)). |
| **Temp Check** | An optional informal forum poll in the Temperature Check category, the first lifecycle phase before a draft ([process](https://docs.ens.domains/dao/governance/process/)). |
| **Quorum** | Minimum token participation for a vote to count; the ENS threshold is set per [proposal type](../01-governance/proposals.md) ([process](https://docs.ens.domains/dao/governance/process/)). |
| **Governor** | The on-chain [OZ Governor](https://www.tally.xyz/gov/ens) holding PROPOSER/EXECUTOR roles on the timelock; surfaced via Tally/Cactus and Agora. |
| **Timelock** | The [OZ TimelockController](https://docs.ens.domains/dao/proposals/0.1/) that enforces a minimum delay before an approved executable runs (see [proposal types](../01-governance/proposals.md)). It is also the [DAO Wallet / treasury custodian](../02-contracts-and-multisigs/addresses.md). |
| **Endowment** | The DAO's long-term reserve, [managed by karpatkey](https://discuss.ens.domains/t/updated-endowment-proposal-karpatkey-steakhouse-financial/14799) in a Safe owned solely by the timelock. |
| **Roles Modifier** | A [Zodiac Roles Modifier](https://docs.ens.domains/dao/proposals/3.4/) on the Endowment Safe that whitelists exactly which protocols/actions karpatkey may execute (non-custodial; karpatkey cannot self-grant permissions). |
| **Allowance Module** | A Safe module on the Endowment Safe permitting karpatkey's recurring monthly management fee to be paid without a separate vote each time. |
| **Superfluid stream** | Continuous-payment mechanism used to pay [SPP](https://discuss.ens.domains/t/ep-6-13-executable-service-provider-program-season-2-implementation/20971) providers: the timelock funds a Stream Management Pod that forwards each provider's stream. |
| **Copeland / ranked-choice** | The ranked-choice method used for [steward elections](../01-governance/elections.md) and multi-option votes (e.g. the [Term 7 WG vote](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107)). |
| **SPP (Service Provider Program)** | DAO program funding ecosystem service providers via streamed payments; [SPP2 implemented by EP6.13](https://discuss.ens.domains/t/ep-6-13-executable-service-provider-program-season-2-implementation/20971). |
