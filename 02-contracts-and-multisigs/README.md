# 02 — Contracts & Multisigs

How on-chain power is structured in the ENS DAO, and who can sign or veto what. The Meta-Governance WG operates within this hierarchy: it signs WG spend, oversees the endowment relationship, and runs the Security Council initiative.

## Sections

| File | Covers |
|------|--------|
| [contract-hierarchy.md](contract-hierarchy.md) | Token → Governor → Timelock (= DAO Wallet); roles, quorum/threshold, voting period, 2-day timelock. |
| [multisigs.md](multisigs.md) | Working-group Safes (Meta-Gov 3/4 + signers), legacy Ecosystem/Public Goods Safes, the SPP stream safe. |
| [security-council.md](security-council.md) | Legacy `veto.ensdao.eth` vs the 2024 council (cancel-only, expiry) vs the 2026 renewal (temp-check) — **plus the emergency veto trigger procedure.** |
| [ens-protocol-control.md](ens-protocol-control.md) | Root, `.eth` registrar lock, controllers, DNSSEC, NameWrapper — and who admins them. |
| [addresses.md](addresses.md) | ⭐ **Canonical address table.** Every contract and Safe in one place. |

> **Single source of truth for addresses:** [addresses.md](addresses.md). Other files link to it rather than re-listing addresses, to avoid divergence.

## Related

- [01-governance/](../01-governance/) — stewards, proposal lifecycle, the WG model.
- [03-treasury-and-endowment/](../03-treasury-and-endowment/) — treasury pools, endowment custody, fee flows.
- [04-runbook/](../04-runbook/) — operational procedures (signing, verification, compensation runs). The emergency veto procedure now lives in [security-council.md](security-council.md).
