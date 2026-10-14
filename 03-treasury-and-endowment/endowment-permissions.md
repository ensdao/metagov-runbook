# Endowment Permissions (Change-Control)

The Endowment is **non-custodial**: karpatkey holds **no signing key** on the Endowment Safe (`endowment.ensdao.eth`). karpatkey acts only through a **Zodiac Roles Modifier** attached to the Safe, which whitelists exactly which protocols and actions its manager may execute ([Endowment FAQ](https://discuss.ens.domains/t/endowment-frequently-asked-questions-faq/16228)). **karpatkey cannot grant itself new permissions**: the Roles Modifier is owned by the Endowment Safe itself (`owner()` checked on-chain 2026-10-14), so every permission change is an Endowment Safe owner transaction. This page is the single source of truth for that change-control model and the recurring "Update #N" series. All addresses are in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

## Who controls the Endowment Safe (since 2026-08-11)

The executable **"Next Era of ENS DAO: Empowering the ENS Foundation"** ([forum](https://discuss.ens.domains/t/22329), [Tally](https://www.tally.xyz/gov/ens/proposal/80619211450810140112687536515944199882433060764177806587986222097717655810120)) executed on 2026-08-11. At Endowment Safe nonce 33 it replaced the DAO Timelock as the Safe's only owner with a new **EndowmentTimelock** ([tx](https://etherscan.io/tx/0xd38d35f55f4387301b5cdf738aabc16d38189df02cafa50c8a47a70605779422)). The Safe stays 1/1 and the assets did not move.

| Role on the EndowmentTimelock | Holder | Effect |
|---|---|---|
| Minimum delay | 777,600 s = **9 days** (`getMinDelay()`) | Every owner-level Endowment transaction waits 9 days |
| PROPOSER_ROLE | **ENS Foundation Safe** (3/5) | Schedules Endowment transactions; can also cancel them |
| PROPOSER_ROLE | **EndowmentSecurityCouncil** | Cancel-only: its code exposes `veto()`, which calls `cancel()`. See [security-council.md](../02-contracts-and-multisigs/security-council.md#endowment-veto-since-2026-08-11) |
| EXECUTOR_ROLE | Anyone (`address(0)`) | Anyone can execute a ready operation |
| TIMELOCK_ADMIN_ROLE | The EndowmentTimelock itself (the deployer renounced) | Role changes must pass the same 9-day, cancellable path |
| DAO Timelock (`wallet.ensdao.eth`) | **No role** | Not a proposer, not an admin |

Roles verified with `hasRole` on 2026-10-14. In this OpenZeppelin TimelockController version, `cancel()` is gated by PROPOSER_ROLE ([verified source](https://sourcify.dev/#/lookup/0x0bcC3dA6aD796F59288C0961602675E88A2B406C)). The [blockful live review](https://discuss.ens.domains/t/22329/15) reports the same setup and that the deployer renounced admin.

The proposal delegates Endowment stewardship to Foundation governance. Tokenholders keep the power to appoint and remove Foundation directors ([proposal text](https://discuss.ens.domains/t/22329)).

### What the timelock does not cover

The 9-day delay applies to the **owner path** only. Two module paths act on the Endowment Safe without it ([blockful review](https://discuss.ens.domains/t/22329/15); [katherine.eth](https://discuss.ens.domains/t/22329/9)):

- the **Roles Modifier**: karpatkey's day-to-day actions inside the whitelist;
- the **Allowance Module**: the monthly management fee. See [treasury-manager-fees.md](../04-runbook/treasury-manager-fees.md).

Changing either module (new permissions, a new fee delegate, a new allowance) is an owner transaction, so the change itself goes through the 9-day timelock.

## How permissions change

Since Update #10, a permission change runs this path ([blockful review of Update #10](https://discuss.ens.domains/t/22323/5); [Meta-Gov funding request](https://discuss.ens.domains/t/22475)):

1. karpatkey publishes the permissions diff and payload on the forum.
2. blockful verifies the calldata against the stated diff.
3. The **Foundation Safe schedules** the Endowment Safe transaction on the EndowmentTimelock.
4. For **9 days** the Security Council can cancel it through the EndowmentSecurityCouncil.
5. **Anyone executes** it after the delay. Only then can karpatkey use the new permission.

There is **no DAO vote** on this path. The Roles architecture was established by [EP4.5](https://docs.ens.domains/dao/proposals/4.5/) and migrated to V2 by [EP5.12](https://docs.ens.domains/dao/proposals/5.12/), which also enabled ETH→stables conversion via CoW Swap (karpatkey converts inside the policy without a per-swap vote).

**Historical path (Updates up to #9):** the DAO passed an executable proposal; after the 2-day DAO timelock it executed against the Roles Modifier, because the DAO Timelock owned the Endowment Safe.

## The "Update #N" series (owner)

Permission changes arrive as a recurring, roughly quarterly update titled "Endowment permissions to karpatkey / kpk – Update #N".

| Update | Path | Change |
|---|---|---|
| #8 (EP6.38) | DAO executable | Added GHO/FLUID via CoW Swap and Fluid rewards; removed SPK |
| #9 ([EP6.41](https://www.tally.xyz/gov/ens/proposal/39893466662181856279242827854933926689925858494049650894234231038376231891860)) | DAO executable, executed 2026-05-10 at Endowment nonce 32 ([tx](https://etherscan.io/tx/0xcfd0befc4f82d37fb26d0b8c4a56aa99d0514f04edfd8a9c579bd07dad6c5161)) | Last update passed by DAO vote |
| **#10** ([thread 22323](https://discuss.ens.domains/t/22323)) | Foundation-scheduled | Switched the Endowment to a **new Roles Modifier** (`0xa23B…FD59`, v2.1.1) that already carries the current MANAGER policy plus the #10 additions (RWA and fixed-income venues, Morpho vaults, Aave v3 Horizon, Maple swap routing); disabled the old one (`0x7038…0A40`, v2.1.0). No permissions removed |

Update #10 timeline: the Foundation Safe scheduled the switch on 2026-10-02 with a 777,600 s delay ([schedule tx](https://etherscan.io/tx/0x7f8da28caa955cdb18b59eeeff4c8efdfd2d2f6d53db86125e13c869f9f85925)), and it executed on 2026-10-12 at Endowment Safe nonce 34 ([switch tx](https://etherscan.io/tx/0xc756a8224a15eb6d9b9f20a529b15acba184c01e7bea3338539fbebb14ea0664)). karpatkey replaced the module to move off Roles v2.1.0, the version named in an [earlier security disclosure](https://discuss.ens.domains/t/security-update-zodiac-roles-modifier-v2-and-delay-modifier-v1-1-0/22161), and to support the newer MultiSend version ([kpk post](https://discuss.ens.domains/t/22323/4)). Before scheduling, kpk moved ownership of the new module from its test Safe to the Endowment Safe ([kpk post](https://discuss.ens.domains/t/22323/6)).

**Sub-Roles Modifier.** Update #10 also added a kpk-owned Sub-Roles Modifier as a member of the new Roles Modifier. kpk can use it to give a subset of the MANAGER permissions to other keys, but it cannot widen MANAGER: only the owner of the main Roles Modifier (the Endowment Safe) can change MANAGER ([kpk post](https://discuss.ens.domains/t/22323/6)).

Series to date (per [karpatkey reporting](https://reports.kpk.io/ens) and the on-chain switch, _as of 2026-10-14_): EP4.5, EP5.12, EP5.14, EP6.8, EP6.23, EP6.27, EP6.38, [EP6.41](https://docs.ens.domains/dao/proposals/6.41/), Update #10 (no EP number; not a DAO vote).

## Running an Update

| Stage | Owner | Action |
|---|---|---|
| 1. Draft | karpatkey | Publishes the Zodiac permissions diff and payload; opens the forum thread |
| 2. Calldata review | blockful | Verifies the payload matches the stated whitelist diff (continuous governance-security review, see [directory](../directory.md)) |
| 3. Audit | external auditor | Permissions config / calldata audited before going live |
| 4. Schedule | ENS Foundation | Foundation Safe calls `schedule` on the EndowmentTimelock with the 9-day delay |
| 5. Veto window | Security Council | 9 days to cancel via the EndowmentSecurityCouncil if the change is malicious or wrong |
| 6. Execute | anyone | Executes the ready operation on the EndowmentTimelock |

When reviewing, diff the **added/removed** protocols and conditions against the forum specification, and check `owner()` of any new Roles Modifier before it is scheduled (blockful's [action point](https://discuss.ens.domains/t/22323/5)). The ETH→stables conversion and the automated runway top-up both run **inside** this policy. See [treasury-automation.md](treasury-automation.md).

> ⚠️ **Open question:** No ENS-governance source ties a specific external audit firm (e.g. Nethermind, Cyfrin, Ackee) to the per-Update calldata audit; confirm the auditor named in each Update's proposal text before relying on it.
>
> ⚠️ **Open question:** The canonical EP number of the "Empowering the ENS Foundation" executable is not yet on [docs.ens.domains](https://docs.ens.domains/dao/proposals/) → [OPEN-QUESTIONS Q-32](../OPEN-QUESTIONS.md).
