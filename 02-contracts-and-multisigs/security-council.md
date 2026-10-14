# Security Council

The DAO's on-chain emergency brake and a Meta-Gov initiative: a council multisig that can **cancel (veto) a queued malicious proposal** in the Timelock, and nothing else (it cannot schedule, propose, or execute). It has evolved through three generations; the current (2026) council is a **5-of-8** Safe. Since 2026-08-11 the same Safe also holds a second, separate veto over **Endowment** transactions queued on the EndowmentTimelock ([below](#endowment-veto-since-2026-08-11)). Addresses in [addresses.md](addresses.md).

## 1. Legacy `veto.ensdao.eth` (predecessor)

A single-action cancel contract. It could **cancel** a queued timelock transaction, hard-locked to calls from a designated Safe. Approved via social proposal **EP 5.7** ([Introducing veto.ensdao.eth](https://discuss.ens.domains/t/introducing-veto-ensdao-eth/19088)). Conceptually superseded by the 2024 council below.

## 2. The 2024 Security Council (superseded in 2026)

| Item | Detail |
|------|--------|
| Established by | **EP 5.7** (social), **EP 5.10** (social, member confirmation), **EP 5.13** (executable, deployed/wired) |
| Council multisig | 4-of-8 Gnosis Safe |
| Veto contract | `SecurityCouncil.sol`, granted **PROPOSER_ROLE** on the Timelock |
| Powers | **cancel-only**: code exposes only `cancel()` + `extend()` |
| Expiry | cancel power auto-expires **2026-07-24** (unix `1784919179`, ~2 years after deployment) |

**Why cancel-only works.** In the OZ TimelockController, PROPOSER_ROLE is the role that gates `cancel()`. `SecurityCouncil.sol` holds that role but its own code exposes **only** `cancel()` (plus `extend()`), callable solely by the 4-of-8 council Safe, so the council can **veto** (cancel) a queued malicious operation but can never schedule, propose, or execute ([EP 5.13](https://docs.ens.domains/dao/proposals/5.13/); [docs](https://docs.ens.domains/dao/security-council/); [contract](https://github.com/blockful/security-council-ens)). At expiry, anyone may call `renounceTimelockRoleByExpiration()` to permanently strip the role.

Confirmed members (EP 5.10): nick.eth, griff.eth, avsa.eth, lefteris.eth, katherineykwu.eth, fireeyes.eth, brantly.eth, alextnetto.eth ([EP 5.10](https://docs.ens.domains/dao/proposals/5.10/)).

## 3. The 2026 Security Council (current)

The 2024 council's veto power was set to expire 2026-07-24, so the DAO renewed it. Two on-chain attempts:

- **EP 6.48 "Renewal of the Security Council (Term 2)"** was **defeated** (vote 2026-06-29 to 2026-07-05; against 3.86M vs for 1.14M) ([Tally](https://www.tally.xyz/gov/ens/proposal/45402179622316441394139979097514597399865468312011562941203078514615705423505)).
- **"[Executable] Establishing a new Security Council"** then **passed and executed 2026-07-22** (for 4.23M, quorum met), two days before the 2024 veto expired ([Tally](https://www.tally.xyz/gov/ens/proposal/77767899528494238518019756391533686963875234067646094287125791110488147463806), [executed tx](https://etherscan.io/tx/0xb2f732c433471ce5274c77d1fe04bd060389319a3b32dfa26ee16164ef46812f)).

The executed proposal granted **PROPOSER_ROLE** on the Timelock to a new, Nethermind-audited (**NM-0945**, zero findings per the [blockful/security-council-ens README](https://github.com/blockful/security-council-ens)) `SecurityCouncil` contract (`0x2acBf5…ae051`), controlled by a new **5-of-8** council Safe (`0x7101B7…9931`). Addresses in [addresses.md](addresses.md). Same cancel-only design as the 2024 council, plus an `extend()` for future renewals by DAO vote.

> ⚠️ **Open question:** The new council's member roster (named identities for the 8 signer addresses of Safe `0x7101B7…9931`) and the executed proposal's canonical EP/docs number are not yet confirmed from a primary source. The roster is in the [executed proposal](https://www.tally.xyz/gov/ens/proposal/77767899528494238518019756391533686963875234067646094287125791110488147463806).

## Endowment veto (since 2026-08-11)

The executable ["Next Era of ENS DAO: Empowering the ENS Foundation"](https://discuss.ens.domains/t/22329) made a new **EndowmentTimelock** the only owner of the Endowment Safe and gave the council a cancel right over it. The Foundation Safe schedules Endowment transactions; each waits **9 days**. Control model: [endowment-permissions.md](../03-treasury-and-endowment/endowment-permissions.md).

| Item | Detail |
|------|--------|
| Veto contract | `EndowmentSecurityCouncil`, a new instance of the same `SecurityCouncil` code, pointed at the EndowmentTimelock ([verified source](https://sourcify.dev/#/lookup/0x0A9387643ce6291f8C545286675D76bCd0Ba3EdD)) |
| Controlled by | The 2026 council Safe (`owner()`, checked on-chain 2026-10-14), so the same **5-of-8** threshold |
| Powers | `veto(id)` cancels a pending EndowmentTimelock operation; it holds PROPOSER_ROLE only because that role gates `cancel()` |
| Window | The 9-day EndowmentTimelock delay |
| Expiry | `expiration()` = 1849227635 = **2028-08-07**; after that anyone can call `renounceTimelockRoleByExpiration()` |
| Renewal | `extend()` is callable **only by the EndowmentTimelock**, so a renewal must be scheduled by the Foundation Safe; the DAO Timelock cannot call it ([verified source](https://sourcify.dev/#/lookup/0x0A9387643ce6291f8C545286675D76bCd0Ba3EdD)) |

In the proposal thread, Alexu wrote for the Foundation that it will commit, in its published treasury policy, to queue the renewal no later than six months before expiry ([forum](https://discuss.ens.domains/t/22329/16)). The proposal describes this cancel right as a technical safeguard, not a general veto over Foundation policy ([proposal text](https://discuss.ens.domains/t/22329)).

## Emergency veto procedure

To stop a malicious executable proposal before it can run:

1. **Detect** a malicious executable proposal that has passed and is **queued in the Timelock** (inside the minimum 2-day delay window before it can execute).
2. **Convene the council**: at least **5 of the 8** signers must agree to veto (current 2026 council).
3. **Cancel**: the council Safe calls the cancel path on the `SecurityCouncil` contract, which calls `cancel()` on the Timelock for that queued operation. The proposal can no longer execute.
4. **Communicate**: post the action and rationale to the [Meta-Governance category](https://discuss.ens.domains/c/meta-governance/28).

The 2-day timelock delay is the window this procedure operates in. See [contract-hierarchy.md](contract-hierarchy.md) for the Timelock and PROPOSER_ROLE mechanics.

**Endowment transactions** use the same steps with two changes: the queue to watch is the **EndowmentTimelock** (9-day window), and the council Safe calls `veto(id)` on the **EndowmentSecurityCouncil**, not on the DAO `SecurityCouncil` contract. Addresses in [addresses.md](addresses.md).

## Related

- Council Safes, both veto contracts, and legacy `veto.ensdao.eth` addresses: [addresses.md](addresses.md).
- Annotated EP timeline (EP 5.7 / 5.10 / 5.13 / renewal): [../reference/governance-history.md](../reference/governance-history.md).
- Signing procedures and anti-phishing verification: [../04-runbook/](../04-runbook/).
