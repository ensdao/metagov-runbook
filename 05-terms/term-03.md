# Term 3: First Term 2023 (Q1/Q2 2023)

**Dates:** 2023-01-01 09:00 UTC – 2023-06-30 · **Cycle:** 6-month (stewards elected Dec 2022, term began Jan 1 2023) · **WGs active:** Meta-Governance, ENS Ecosystem, Public Goods.

EP prefix this term is `EP3.x` ([Basics: EP numbering](https://basics.ensdao.org/executable-proposals)). This was a three-WG term; the Community WG had already been [dissolved](https://discuss.ens.domains/t/dissolve-the-community-working-group/12970) at the end of Term 1.

Source: [The Block: DAO votes to elect stewards for three WGs](https://www.theblock.co/post/194045/ens-dao-voting-to-elect-stewards-to-helm-three-working-groups).

## Stewards

| WG | Name (ENS) | Role |
|---|---|---|
| Meta-Governance | [Katherine Wu (katherine.eth)](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) | Lead steward |
| Meta-Governance | [nick.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| Meta-Governance | [simona.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| ENS Ecosystem | [slobo.eth](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) | Lead steward |
| ENS Ecosystem | [limes.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| ENS Ecosystem | [yambo.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| Public Goods | [coltron.eth](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) | Lead steward |
| Public Goods | [avsa.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| Public Goods | [vegayp.eth](https://www.coindesk.com/business/2022/12/15/ethereum-name-service-dao-votes-on-stewards-for-three-working-groups) | Steward |
| DAO-wide | [coltron.eth](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) | Secretary (Jan 5 2023; stepped down) |
| DAO-wide | [limes.eth](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) | Secretary (from May 18 2023, per Rule 9.2) |

## Funding

All three WG requests were executed together on-chain via **[EP3.2](https://discuss.ens.domains/t/ep-3-2-executable-q1-q2-2023-working-group-funding/16123)**.

| WG | Proposal | Amount (as stated) | Window |
|---|---|---|---|
| Meta-Governance | [EP3.1.2](https://docs.ens.domains/dao/proposals/3.1.2/) | 364,000 USDC + 125 ETH + 3,500 ENS | Q1/Q2 2023 |
| ENS Ecosystem | [EP3.1.1](https://docs.ens.domains/dao/proposals/3.1.1/) | 935,000 USDC + 254 ETH | Q1/Q2 2023 |
| Public Goods | [EP3.1.3](https://docs.ens.domains/dao/proposals/3.1.3/) | 250,000 USDC + 50 ETH | Q1/Q2 2023 |

## Compensation

No standalone compensation-standard proposal this term. Compensation was budgeted in aggregate inside the Meta-Gov funding request **[EP3.1.2](https://docs.ens.domains/dao/proposals/3.1.2/)**, which states only: Working Group Steward compensation totaling **$144k USDC + 3,000 ENS**, plus Secretary compensation of **$40k USDC**.

> ⚠️ **Open question:** Per-role / per-person rates (steward vs lead vs secretary, and headcount per rate) were never stated for Term 3, only the aggregate figures above. Standardized per-role rates were introduced later, in [Term 4 (Nov 2 2023)](https://discuss.ens.domains/t/ens-dao-steward-compensation/18063). Do not infer Term 3 rates.

## Multisig

Each WG operated through its own Safe (see the canonical [addresses table](../02-contracts-and-multisigs/addresses.md#working-group--stream-safes)):

- **Meta-Governance** `main.mg.wg.ens.eth`: `0x91c3…d39b`, **3/4** ([confirmed via Safe API](https://safe-transaction-mainnet.safe.global/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b)).
- **ENS Ecosystem** `ens-ecosystem.pod.xyz`: `0x2686…5d03` ([per EP3.2](https://discuss.ens.domains/t/ep-3-2-executable-q1-q2-2023-working-group-funding/16123)).
- **Public Goods** `ens-publicgoods.pod.xyz`: `0xcD42…D87d` ([per EP3.2](https://discuss.ens.domains/t/ep-3-2-executable-q1-q2-2023-working-group-funding/16123)).

> ⚠️ **Open question:** The Ecosystem and Public Goods Safe thresholds were not confirmed via the Safe API for Term 3, and the Meta-Gov Safe API returns only the *current* owner set. The exact Term 3 signer roster (relevant to the Coltron→Limes secretary/multisig handover in May 2023) is unverified.

## Activity

- [EP3.1.1 / EP3.1.2 / EP3.1.3](https://docs.ens.domains/dao/proposals/3.1.2/): Q1/Q2 2023 funding requests (Ecosystem, Meta-Gov, Public Goods); executed by [EP3.2](https://discuss.ens.domains/t/ep-3-2-executable-q1-q2-2023-working-group-funding/16123).
- [EP3.3](https://docs.ens.domains/dao/proposals/3.3/): [Executable] Sell ETH to USDC.
- [EP3.4](https://docs.ens.domains/dao/proposals/3.4/): [Executable] Fund the Endowment (first tranche): karpatkey selected; 16,000 ETH to the Endowment + 150 ETH to the Meta-Gov pod for karpatkey/Steakhouse fees.
- [EP3.5](https://docs.ens.domains/dao/proposals/3.5/): [Executable] Activate new .eth Controller and Reverse Registrar.
- [EP3.6](https://docs.ens.domains/v/governance/governance-proposals/term-3): [Social] Election of new ENS Foundation director.
- [EP3.7](https://docs.ens.domains/v/governance/governance-proposals/term-3): [Social] Approval of ENS Name Normalization Standard.
- [WG Lead Steward + Secretary appointments](https://discuss.ens.domains/t/working-group-lead-stewards-secretary-appointment/15787) (Jan 5 2023).
