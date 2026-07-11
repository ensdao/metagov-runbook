# Treasury Automation (EP6.39)

[**EP6.39: Treasury Flow Automation**](https://discuss.ens.domains/t/executable-treasury-flow-automation/21923) (author coltron.eth; Cyfrin-audited Mar 2026; executed) replaced a set of manual, per-vote treasury chores with a standing, policy-bounded flow. The DAO vote sets the policy; karpatkey operates inside it; the inbound sweep is permissionless.

## What it automates

| Mechanism | Effect | Constraint |
|-----------|--------|------------|
| **Registrar Manager** | Permissionless `withdraw()` sweeps registrar ETH **straight to the Endowment** (`0x4F2083…FE64`) | Anyone can call; routes to the endowment only |
| **Zodiac runway permission** | karpatkey can send funds to `wallet.ensdao.eth` (Timelock) **without a vote** to fund operating runway | **ETH and USDC only**, **to the Timelock only**: no other token, no other address |
| **ETH→stables conversion** | karpatkey converts inside the Roles policy via **CoW Swap** (enabled by [EP5.12](https://docs.ens.domains/dao/proposals/5.12/)) | Within the Roles V2 whitelist; no per-swap vote |

## Runway policy

- The **Timelock maintains a 6-month USDC runway** (~$8M at current spend).
- karpatkey **recalculates each quarter** and tops up the Timelock when it falls below threshold.

> ⚠️ **Open question:** EP6.39 also references a longer multi-year stablecoin runway held at the **endowment** level; sources report it inconsistently as two-year vs three-year. The 6-month **Timelock** figure is confirmed; the exact endowment-level horizon is not pinned.

See [revenue-flow.md](revenue-flow.md) for the end-to-end path and [endowment-permissions.md](endowment-permissions.md) for how the Roles policy is changed.

## Deprecated (historical)

These predate EP6.39 and should be treated as historical:

- **Manual ETH→USDC TWAP swaps**: [EP3.3](https://docs.ens.domains/dao/proposals/3.3/) (CoW/Milkman) and the ENS TWAP Multisig (EP6.1). Superseded: karpatkey now converts on-chain inside the Roles policy.
- **One-off "transfer USDC from endowment to `wallet.ensdao.eth`" votes**: EP6.32 ($2.5M), EP6.37 ($900k). Superseded by the standing Zodiac runway permission.

Addresses for the Registrar Manager, Roles Modifier, and manager EOA are in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).
