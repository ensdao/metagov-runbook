# ⭐ Canonical Address Table

**Single source of truth** for ENS DAO contract and Safe addresses **and Safe thresholds**. Other runbook files link here rather than re-listing these values. Verify on-chain before signing — see anti-phishing guidance in [04-runbook/verification-and-safety.md](../04-runbook/verification-and-safety.md).

## Governance core

| Name | ENS | Address | Type / threshold | Source |
|------|-----|---------|------------------|--------|
| ENS token | `token.ensdao.eth` | `0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72` | ERC20Votes, 100M | [docs](https://basics.ensdao.org/ens-dao-contracts) |
| ENS Governor | `governor.ensdao.eth` | `0x323A76393544d5ecca80cd6ef2A560C6a395b7E3` | OZ Governor | [docs](https://basics.ensdao.org/ens-dao-contracts) |
| ENS Timelock = DAO Wallet | `wallet.ensdao.eth` | `0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7` | OZ TimelockController (not a Safe) | [docs](https://basics.ensdao.org/ens-dao-contracts) |

## Working-group & stream Safes

| Name | ENS | Address | Type / threshold | Source |
|------|-----|---------|------------------|--------|
| Meta-Gov main Safe | `main.mg.wg.ens.eth` | `0x91c32893216dE3eA0a55ABb9851f581d4503d39b` | Safe, 3/4 | [Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/) |
| SPP stream safe | `stream.mg.wg.ens.eth` | `0xB162Bf7A7fD64eF32b787719335d06B2780e31D1` | Safe, 1/2 | [Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0xB162Bf7A7fD64eF32b787719335d06B2780e31D1/) |
| Ecosystem main Safe (legacy) | `main.eco.wg.ens.eth` | `0x2686A8919Df194aA7673244549E68D42C1685d03` | Safe, 3/4 | [Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0x2686A8919Df194aA7673244549E68D42C1685d03/) |
| Public Goods main Safe (legacy) | `main.pg.wg.ens.eth` | `0xcD42b4c4D102cc22864e3A1341Bb0529c17fD87d` | Safe, 3/4 | [Safe API](https://api.safe.global/tx-service/eth/api/v1/safes/0xcD42b4c4D102cc22864e3A1341Bb0529c17fD87d/) |

## Endowment & treasury automation

| Name | ENS | Address | Type / threshold | Source |
|------|-----|---------|------------------|--------|
| Endowment Safe | `endowment.ensdao.eth` | `0x4F2083f5fBede34C2714aFfb3105539775f7FE64` | Safe, 1/1 (owner = Timelock) | [EP 3.4](https://docs.ens.domains/dao/proposals/3.4/) |
| Zodiac Roles Modifier V2 | — | `0x703806E61847984346d2D7DDd853049627e50A40` | Roles Modifier (karpatkey whitelist) | [EP 5.12](https://docs.ens.domains/dao/proposals/5.12/) |
| Endowment manager EOA | — | `0xb423e0f6E7430fa29500c5cC9bd83D28c8BD8978` | karpatkey manager (acts via Roles) | [Endowment FAQ](https://discuss.ens.domains/t/endowment-frequently-asked-questions-faq/16228) |
| Allowance Module | — | `0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134` | Safe Allowance Module (30 ETH, ~25d reset) | [EP 6.2](https://docs.ens.domains/dao/proposals/6.2/) |
| karpatkey fee Safe | — | `0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C` | Safe, 3/7 (fee recipient) | [Endowment FAQ](https://discuss.ens.domains/t/endowment-frequently-asked-questions-faq/16228) |
| Registrar Manager (EP 6.39) | — | `0x62627681D92e36b9aeE1D9A6BF181373ccd42552` | Owns controllers; permissionless `withdraw()` → endowment | [EP 6.39 thread](https://discuss.ens.domains/t/executable-treasury-flow-automation/21923) |
| Hedgey BatchPlanner | — | `0x3466EB008EDD8d5052446293D1a7D212cb65C646` | Token-vesting batch planner | [EP 5.26 context](https://www.tally.xyz/gov/ens) |

## Security Council

| Name | ENS | Address | Type / threshold | Source |
|------|-----|---------|------------------|--------|
| SecurityCouncil contract (2024) | — | `0xb8fa0ce3f91f41c5292d07475b445c35ddf63ee0` | Holds PROPOSER_ROLE; cancel-only | [EP 5.13](https://docs.ens.domains/dao/proposals/5.13/) |
| Security Council multisig | — | `0xaA5cD05f6B62C3af58AE9c4F3F7A2aCC2Cdc2Cc7` | Safe, 4/8 | [docs](https://docs.ens.domains/dao/security-council/) |
| Legacy `veto.ensdao.eth` | `veto.ensdao.eth` | `0x552DF471a4c7Fea11Ea8d7a7b0Acc6989b902a95` | Predecessor cancel contract | [EP 5.7 thread](https://discuss.ens.domains/t/introducing-veto-ensdao-eth/19088) |

> The 2026 Nethermind-audited renewal contract has **no on-chain address yet** (temp-check stage). See [security-council.md](security-council.md).

## ENS protocol contracts

| Name | ENS | Address | Type | Source |
|------|-----|---------|------|--------|
| Root | `root.ens.eth` | `0xaB528d626EC275E3faD363fF1393A41F581c5897` | TLD allocation (owner resolves to `0x4Fe4e666…e3e0e8`) | [EP 4.10](https://docs.ens.domains/dao/proposals/4.10/) |
| ENS Registry | — | `0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e` | Root registry | [deployments](https://docs.ens.domains/learn/deployments/) |
| `.eth` BaseRegistrar | — | `0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85` | `.eth` registrations (ERC-721) | [deployments](https://docs.ens.domains/learn/deployments/) |
| ETHRegistrarController (current) | — | `0x59E16fcCd424Cc24e280Be16E11Bcd56fb0CE547` | Registration/renewal | [deployments wiki](https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments) |
| ETHRegistrarController (alias / legacy) | `controller.ens.eth` | `0x253553366Da8546fC250F225fE3d25d0C782303b` | Older — alias lags source of truth | [deployments wiki](https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments) |
| DNSRegistrar / DNSSEC | — | `0xB32cB5677a7C971689228EC835800432B339bA2B` | DNS-proof claims | [deployments](https://docs.ens.domains/learn/deployments/) |
| NameWrapper | — | `0xD4416b13d2b3a9aBae7AcD5D6C2BbDBE25686401` | ERC-1155 wrap + fuses | [deployments](https://docs.ens.domains/learn/deployments/) |
| PublicResolver | — | `0xF29100983E058B709F3D539b0c765937B804AC15` | Default resolver | [deployments](https://docs.ens.domains/learn/deployments/) |

> ⚠️ **Open question:** `controller.ens.eth` resolves to the older `0x2535…303b` while the deployments wiki lists `0x59E1…eA547` as the active ETHRegistrarController. Confirm whether the alias is intentionally retained or simply not updated.

## Notes

- The Timelock and DAO Wallet are **one address**, two ENS names. ENS docs sometimes loosely call it "the Metagov multisig" — it is not; that is the separate Meta-Gov Safe above.
- The karpatkey monthly management fee lands at the **fee Safe `0x58e6…`**, not the Meta-Gov Safe; the Meta-Gov Safe is the Allowance Module *delegate* (per EP 6.2), not the recipient.
- Do **not** confuse the legacy pre-DAO `ENS: Multisig` (`0x911143d946bA5d467BfC476491fdb235fEf4D667`) with any active treasury or WG Safe.
