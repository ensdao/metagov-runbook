# Treasury Overview

The ENS DAO treasury is **three managed pools**, all ultimately controlled by on-chain governance. The Meta-Governance WG is the working group accountable for overseeing them.

## The three pools

| Pool | Custody | Managed how |
|------|---------|-------------|
| **Main treasury** | ENS Timelock / `wallet.ensdao.eth` | Funds leave only via an executed proposal (after the 2-day timelock) |
| **Endowment** | `endowment.ensdao.eth` Safe, **owned 1/1 by the Timelock** | karpatkey operates it non-custodially via a Zodiac Roles whitelist — see [endowment.md](endowment.md) |
| **WG operating budgets** | Working Group multisig(s) | Funded per term from the Timelock; stewards disburse within budget |

## Timelock = the custodial root

The [ENS Timelock](https://docs.ens.domains/dao/governance/process/) **is** the DAO Wallet — one address, two names (`wallet.ensdao.eth`). It is an OpenZeppelin `TimelockController` (not a Safe), holds the bulk of liquid DAO funds, owns the core ENS protocol contracts, and is the **sole owner of the Endowment Safe** ([EP3.4](https://docs.ens.domains/dao/proposals/3.4/)). Every executable spend originates here after a minimum 2-day delay. It is also the only address `.eth` registration revenue can be withdrawn to — see [revenue-flow.md](revenue-flow.md).

> Addresses for all of the above live in [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md).

## Reading the live numbers

Prefer live dashboards over hardcoded figures — _as of 2026-06-20_:

- **[Anticapture — ENS](https://app.anticapture.com/ens)** — total / liquid / ENS-token treasury split, votable supply, treasury-vs-attack metrics.
- **[karpatkey ENS dashboard](https://reports.kpk.io/ens)** — endowment AUM, asset allocation (ETH vs stablecoins), monthly yield, capital-utilisation ratio. The canonical public reporting surface (legacy `reports.karpatkey.com/ens` redirects here).
- **[karpatkey Dune](https://dune.com/kpk/ens-dao-governance)** — governance/treasury metrics.

The DAO diversifies out of pure-ETH risk over time; the governing policy is the **Investment Policy Statement** ([EP5.20](https://docs.ens.domains/dao/proposals/5.20/)), detailed in [endowment.md](endowment.md).
