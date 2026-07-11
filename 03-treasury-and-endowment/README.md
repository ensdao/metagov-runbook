# Treasury & Endowment

How the ENS DAO treasury is structured, where the money flows, and the controls the Meta-Governance Working Group operates. The DAO holds funds in three places: the **Timelock** (main treasury), the **Endowment** (a karpatkey-managed reserve), and **Working Group multisigs**, all rooted in on-chain governance.

> Addresses are **not** re-listed here. The canonical address table is [`../02-contracts-and-multisigs/addresses.md`](../02-contracts-and-multisigs/addresses.md). Link to it; never duplicate.

## Sections

| File | What it covers |
|------|----------------|
| [treasury-overview.md](treasury-overview.md) | The three pools, Timelock custody, live dashboards |
| [revenue-flow.md](revenue-flow.md) | Registration fees → controller → withdraw → endowment |
| [treasury-automation.md](treasury-automation.md) | EP6.39 Treasury Flow Automation, Zodiac runway top-ups, deprecated manual swaps |
| [endowment.md](endowment.md) | karpatkey mandate, IPS, funding tranches, reporting |
| [endowment-permissions.md](endowment-permissions.md) | Zodiac Roles Modifier V2 change-control & the "Update #N" series |
| [service-provider-program.md](service-provider-program.md) | SPP1 → SPP2 budgets and the Superfluid stream pod |
| [spending-controls.md](spending-controls.md) | Who-signs-what authorization matrix; Constitution Article III |

## Related

- [`../01-governance/`](../01-governance/): proposal lifecycle that authorizes every spend
- [`../02-contracts-and-multisigs/`](../02-contracts-and-multisigs/): addresses, thresholds, signer sets
- [karpatkey ENS dashboard](https://reports.kpk.io/ens) · [Anticapture ENS](https://app.anticapture.com/ens): live figures
