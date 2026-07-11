# Endowment Permissions (Change-Control)

The Endowment is **non-custodial**: the Endowment Safe (`endowment.ensdao.eth`) is owned 1/1 by the DAO Timelock, and karpatkey holds **no signing key**. karpatkey acts only through a **Zodiac Roles Modifier V2** attached to the Safe, which whitelists exactly which protocols and actions its manager EOA may execute ([Endowment FAQ](https://discuss.ens.domains/t/endowment-frequently-asked-questions-faq/16228)). **karpatkey cannot grant itself new permissions** — every new integration or parameter change requires a DAO executable proposal. This page is the single source of truth for that change-control model and the recurring "Update #N" series. Endowment Safe, Roles Modifier V2, and manager EOA addresses are in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

## How permissions change

Changing what karpatkey can do — add a protocol, enable a swap venue, remove a deprecated one — always runs the executable path:

1. The integration / parameter change is proposed together with its Zodiac permissions diff.
2. The DAO passes an **executable proposal** that updates the Roles V2 config.
3. After the minimum 2-day timelock, the change executes against the Roles Modifier. Only then can karpatkey use the new permission.

This is the governance gate through which the DAO controls everything the manager can do — the core of the financial-controls runbook. The Roles architecture was established by [EP4.5](https://docs.ens.domains/dao/proposals/4.5/) and migrated to V2 by [EP5.12](https://docs.ens.domains/dao/proposals/5.12/), which also enabled ETH→stables conversion via CoW Swap (karpatkey converts inside the policy without a per-swap vote).

## The "Update #N" series (owner)

Permission changes arrive as a recurring, roughly quarterly executable:

> **`[EP X.Y] [Executable] Endowment permissions to karpatkey – Update #N`**

Each Update adds or removes whitelisted protocols/actions. Example: **EP6.38 (Update #8)** added GHO/FLUID via CoW Swap and Fluid rewards, and removed SPK. The latest is **[EP6.41 — Update #9](https://www.tally.xyz/gov/ens/proposal/39893466662181856279242827854933926689925858494049650894234231038376231891860)**.

Series to date (per [karpatkey reporting](https://reports.kpk.io/ens), as of 2026-06-20): EP4.5, EP5.12, EP5.14, EP6.8, EP6.23, EP6.27, EP6.38, [EP6.41](https://docs.ens.domains/dao/proposals/6.41/).

## Running an Update

| Stage | Owner | Action |
|---|---|---|
| 1. Draft | karpatkey | Publishes the Zodiac permissions diff; opens the forum thread; creates the Tally draft |
| 2. Calldata review | blockful | Verifies the executable calldata matches the stated whitelist diff (continuous governance-security review — see [directory](../directory.md)) |
| 3. Audit | external auditor | Permissions config / calldata audited before going live |
| 4. Executable | DAO | Governor executable vote, then the 2-day timelock before execution — thresholds in [`../01-governance/proposals.md`](../01-governance/proposals.md) |

When reviewing, diff the **added/removed** protocols and conditions against the proposal abstract. The [Security Council](../02-contracts-and-multisigs/security-council.md) veto is the emergency backstop if a malicious permissions change is ever queued. The ETH→stables conversion and the automated runway top-up both run **inside** this policy — see [treasury-automation.md](treasury-automation.md).

> ⚠️ **Open question:** Whether the Roles Modifier V2 instance listed in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md) is still the sole/current instance, or has been superseded by a later Update — confirm against the Zodiac diff in the most recent Update proposal.
>
> ⚠️ **Open question:** No ENS-governance source ties a specific external audit firm (e.g. Nethermind, Cyfrin, Ackee) to the per-Update calldata audit; confirm the auditor named in each Update's proposal text before relying on it.
