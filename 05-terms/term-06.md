# Term 6 — Calendar 2025

- **Label:** Term 6 (Calendar 2025)
- **Dates:** nominally [1 Jan 2025 09:00 UTC – 31 Dec 2025](https://discuss.ens.domains/t/term-6-ens-dao-steward-nominations-and-election-process/19913). The clean end date was superseded: the [ENS Retro proposal (EP 6.26)](https://snapshot.box/#/s:ens.eth/proposal/0x8d16992852893f05b23b0e26de27c9e6b2a8de1193c991e14f81ef13cd943517) kept Term 6 stewards in place through the ~4-month retro window (Dec 2025 – Apr 2026) and deferred elections; Term 7 nominations were committed to begin 1 Apr 2026.
- **Cycle:** annual (per [EP4.8](https://docs.ens.domains/dao/proposals/4.8/))
- **WGs active:** Meta-Governance, ENS Ecosystem, Public Goods
- **Election:** held [10 Dec 2024 09:00 UTC – 15 Dec 2024 09:00 UTC](https://discuss.ens.domains/t/term-6-ens-dao-steward-nominations-and-election-process/19913); nominations 6–9 Dec 2024.

> ⚠️ **Open question:** A single ratified "new Term 6 end date" is not cleanly stated in one source — the retro extended stewards into 2026 with Term 7 nominations committed to 1 Apr 2026, but exact extension start/end timestamps remain unpinned.

## Stewards

Roster per the [ENS DAO Term 6 Dashboard](https://discuss.ens.domains/t/ens-dao-term-6-dashboard/20076) and Snapshot election ballots.

| WG | Name (ENS) | Role |
|----|------------|------|
| Meta-Governance | 5pence.eth (Spence) | Lead steward |
| Meta-Governance | [daostrat.eth (Cam)](https://snapshot.box/#/s:ens.eth/proposal/0xd42e261f9bf298bb5a793ee230a5f1a164db6c47e9656aaa83cf2ad4c4798832) | Steward |
| Meta-Governance | [netto.eth (Alex)](https://snapshot.box/#/s:ens.eth/proposal/0xd42e261f9bf298bb5a793ee230a5f1a164db6c47e9656aaa83cf2ad4c4798832) | Steward |
| ENS Ecosystem | slobo.eth | Lead steward |
| ENS Ecosystem | [limes.eth](https://snapshot.box/#/s:ens.eth/proposal/0xd06e971e596ea5d9704372184503fdacbbe69c9ee7aa9e6af1acba4355b5954f) | Steward |
| ENS Ecosystem | [daemon.eth (Donnie)](https://snapshot.box/#/s:ens.eth/proposal/0xd06e971e596ea5d9704372184503fdacbbe69c9ee7aa9e6af1acba4355b5954f) | Steward |
| Public Goods | simona.eth | Lead steward |
| Public Goods | [coltron.eth](https://snapshot.box/#/s:ens.eth/proposal/0xb33e76201100b32a09f8aa367ad564e910f45b845318715439fee7e4978efd6b) | Steward |
| Public Goods | [sovereignsignal.eth (Sov)](https://snapshot.box/#/s:ens.eth/proposal/0xb33e76201100b32a09f8aa367ad564e910f45b845318715439fee7e4978efd6b) | Steward |
| DAO-wide | [limes.eth](https://discuss.ens.domains/t/ens-dao-term-6-dashboard/20076) | Secretary |

## Funding

Two funding windows; each WG sub-proposal was bundled into a single collective Executable.

| WG | Proposal | Amount (as stated) | Window |
|----|----------|--------------------|--------|
| Meta-Governance | [EP 6.6.1](https://docs.ens.domains/dao/proposals/6.6.1/) (Social) → [EP 6.11](https://docs.ens.domains/dao/proposals/6.11/) | 589,000 USDC + 100,000 ENS | Apr 2025 – Oct 2025 |
| Public Goods | [EP 6.6.2](https://docs.ens.domains/dao/proposals/6.6.2/) (Social) → [EP 6.11](https://docs.ens.domains/dao/proposals/6.11/) | 356,000 USDC | Apr 2025 – Oct 2025 |
| ENS Ecosystem | No April-2025 request | — | Apr 2025 |
| Meta-Governance | EP 6.24.1 (Social) → [EP 6.28](https://discuss.ens.domains/t/ep-6-28-executable-collective-working-group-funding-request-oct-2025/21654) | 379,000 USDC | Oct 2025 – Apr 2026 |
| ENS Ecosystem | [EP 6.24.2](https://docs.ens.domains/dao/proposals/6.24.2/) (Social) → [EP 6.28](https://discuss.ens.domains/t/ep-6-28-executable-collective-working-group-funding-request-oct-2025/21654) | 470,000 USDC | Oct 2025 – Apr 2026 |
| Public Goods | EP 6.24.3 (Social) → [EP 6.28](https://discuss.ens.domains/t/ep-6-28-executable-collective-working-group-funding-request-oct-2025/21654) | 110,000 USDC + 15 ETH | Oct 2025 – Apr 2026 |

## Compensation

Set by the [ENS DAO Steward Compensation Structure — Term 6](https://discuss.ens.domains/t/ens-dao-steward-compensation-structure-term-6/19739) (Social proposal by 5pence.eth, posted 18 Oct 2024, passed on Snapshot). Per EP4.8, Meta-Gov defined these guidelines ahead of the Term 6 nomination window.

| Role | Monthly (USDC) | Annual (USDC) |
|------|----------------|----------------|
| Steward (6) | $4,000 | $48,000 |
| Lead Steward (3) | $5,500 | $66,000 |
| Secretary (1) | $5,500 | $66,000 |
| Scribe (1) | $3,000 | $36,000 |

Total term budget stated as $588,000 USDC. Each steward also receives ENS tokens equal in value to total annual USDC comp, distributed 1 Jul on 2-year linear vesting, priced on the Jan 1 – Jul 1 6-month average.

> ⚠️ **Open question:** The EP id of the Term 6 compensation proposal is unconfirmed — a forum read labeled it "EP 5.18" but this was not found in the docs proposals index; the rate table and $588,000 total are from an LLM extraction not verified line-by-line.

## Multisig

WG Safes (3-of-4, confirmed on-chain). See [addresses.md](../02-contracts-and-multisigs/addresses.md) for the canonical table.

| WG | Safe | Threshold |
|----|------|-----------|
| Meta-Governance (main.mg.wg.ens.eth) | `0x91c3…d39b` | 3 of 4 |
| ENS Ecosystem (main.eco.wg.ens.eth) | `0x2686…5d03` | 3 of 4 |
| Public Goods | `0xcD42…D87d` | 3 of 4 |

> ⚠️ **Open question:** The Ecosystem Safe is 4 owners / threshold 3 on-chain (one owner is the Meta-Gov Safe), while forum framing describes Ecosystem multisigs as "3 of 5" (3 stewards + secretary + Meta-Gov multisig). The on-chain config and documented governance model need reconciling.

## Activity

- [EP 6.26 [Social] ENS Retro](https://snapshot.box/#/s:ens.eth/proposal/0x8d16992852893f05b23b0e26de27c9e6b2a8de1193c991e14f81ef13cd943517) — passed (For 1,134,046 vs Against 755,763); extended Term 6 stewards through the retro window and deferred Term 7 elections.
- [Temp Check: Metagov Update — WG Operations During the ENS Retro](https://discuss.ens.domains/t/temp-check-metagov-update-working-group-operations-during-the-ens-retro/21781) — clarified steward continuation and suspended elections (new date committed 1 Apr 2026).
- [EP 6.11 [Executable] Collective WG Funding Request (April 2025)](https://discuss.ens.domains/t/6-6-1-social-april-funding-request-ens-meta-governance-working-group-term-6/20536) — executed; disbursed 945,000 USDC + 100,000 ENS to Meta-Gov + Public Goods.
- [EP 6.28 [Executable] Collective WG Funding Request (Oct 2025)](https://discuss.ens.domains/t/ep-6-28-executable-collective-working-group-funding-request-oct-2025/21654) — executed; 959,000 USDC + 15 ETH across all three WGs.
- [EP 6.32 [Executable] Transfer $2.5M USDC from Endowment to wallet.ensdao.eth](https://discuss.ens.domains/t/ep-6-32-executable-transfer-2-5m-usdc-from-endowment-to-wallet-ensdao-eth/21882) — Meta-Gov-led treasury/endowment operation.
- [Path forward on Working Groups for Term 7](https://discuss.ens.domains/t/path-forward-on-working-groups-for-term-7/22107) — outcome made Meta-Governance the sole WG for Term 7.
- [Term 6 Proposal Bulletin](https://discuss.ens.domains/t/term-6-proposal-bulletin/20157) — running index of Term 6 EPs.
- [ENS DAO Term 6 Dashboard](https://discuss.ens.domains/t/ens-dao-term-6-dashboard/20076) — canonical roster + roles.
