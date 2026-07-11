# Security Council

The DAO's on-chain emergency brake and a Meta-Gov initiative: a **4-of-8 multisig** that can **cancel (veto) a queued malicious proposal** in the Timelock, and nothing else (it cannot schedule, propose, or execute). It has evolved through three generations. Addresses in [addresses.md](addresses.md).

## 1. Legacy `veto.ensdao.eth` (predecessor)

A single-action cancel contract. It could **cancel** a queued timelock transaction, hard-locked to calls from a designated Safe. Approved via social proposal **EP 5.7** ([Introducing veto.ensdao.eth](https://discuss.ens.domains/t/introducing-veto-ensdao-eth/19088)). Conceptually superseded by the 2024 council below.

## 2. The 2024 Security Council (current)

| Item | Detail |
|------|--------|
| Established by | **EP 5.7** (social), **EP 5.10** (social, member confirmation), **EP 5.13** (executable, deployed/wired) |
| Council multisig | 4-of-8 Gnosis Safe |
| Veto contract | `SecurityCouncil.sol`, granted **PROPOSER_ROLE** on the Timelock |
| Powers | **cancel-only**: code exposes only `cancel()` + `extend()` |
| Expiry | cancel power auto-expires **2026-07-24** (unix `1784919179`, ~2 years after deployment) |

**Why cancel-only works.** In the OZ TimelockController, PROPOSER_ROLE is the role that gates `cancel()`. `SecurityCouncil.sol` holds that role but its own code exposes **only** `cancel()` (plus `extend()`), callable solely by the 4-of-8 council Safe, so the council can **veto** (cancel) a queued malicious operation but can never schedule, propose, or execute ([EP 5.13](https://docs.ens.domains/dao/proposals/5.13/); [docs](https://docs.ens.domains/dao/security-council/); [contract](https://github.com/blockful/security-council-ens)). At expiry, anyone may call `renounceTimelockRoleByExpiration()` to permanently strip the role.

Confirmed members (EP 5.10): nick.eth, griff.eth, avsa.eth, lefteris.eth, katherineykwu.eth, fireeyes.eth, brantly.eth, alextnetto.eth ([EP 5.10](https://docs.ens.domains/dao/proposals/5.10/)).

## 3. The 2026 renewal (TEMP-CHECK stage, not yet live)

A new **Nethermind-audited** `SecurityCouncil` contract that **re-grants PROPOSER_ROLE before the 2024 council's veto expires on 2026-07-24**, and adds an `extend()` function callable only by the DAO Timelock, so future renewals are a single governance vote with no redeployment. Audit: Nethermind Security review **NM-0945** (2026-06-05, zero findings / "zero points of attention" per the [blockful/security-council-ens README](https://github.com/blockful/security-council-ens)). The renewal action will be `ENSTimelock.grantRole(PROPOSER_ROLE, newContract)`.

> ⚠️ **Open question:** As of 2026-06-20 the renewal is still at **temp-check** ([thread 22145](https://discuss.ens.domains/t/temp-check-renewal-of-the-security-council/22145)). No Snapshot social or executable EP number has been assigned, and the deployed new-contract address and final `grantRole(PROPOSER_ROLE, …)` transaction are not yet on-chain. Re-check after the executable goes live.

## Emergency veto procedure

To stop a malicious executable proposal before it can run:

1. **Detect** a malicious executable proposal that has passed and is **queued in the Timelock** (inside the minimum 2-day delay window before it can execute).
2. **Convene the council**: at least **4 of the 8** signers must agree to veto.
3. **Cancel**: the council Safe calls the cancel path on the `SecurityCouncil` contract, which calls `cancel()` on the Timelock for that queued operation. The proposal can no longer execute.
4. **Communicate**: post the action and rationale to the [Meta-Governance category](https://discuss.ens.domains/c/meta-governance/28).

The 2-day timelock delay is the window this procedure operates in. See [contract-hierarchy.md](contract-hierarchy.md) for the Timelock and PROPOSER_ROLE mechanics.

## Related

- Council 4-of-8 Safe and legacy `veto.ensdao.eth` addresses: [addresses.md](addresses.md).
- Annotated EP timeline (EP 5.7 / 5.10 / 5.13 / renewal): [../reference/governance-history.md](../reference/governance-history.md).
- Signing procedures and anti-phishing verification: [../04-runbook/](../04-runbook/).
