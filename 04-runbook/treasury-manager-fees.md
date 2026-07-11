# Treasury-Manager Fees (karpatkey)

karpatkey is paid two fees for managing the endowment. The **management fee** is automated and monthly; the **performance fee** is settled separately on realized yields ([endowment FAQ/initiation threads](https://discuss.ens.domains/)).

## Fee model

| Fee | Rate | Paid | Cap |
|---|---|---|---|
| Management | 0.5% / yr | **Monthly, in ETH** | ≤ **30 ETH / period** |
| Performance | 10% | Settled on realized yield, in the yield's reference currency | n/a |

Source: [endowment FAQ/initiation threads](https://discuss.ens.domains/).

## ⚠️ Where the fee lands — NOT the Meta-Gov Safe

The recurring management fee is paid **endowment Safe → the karpatkey fee Safe `0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C`** (verify against [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md)) ([Safe Tx Service](https://app.safe.global/)).

> **It does NOT land at the Meta-Gov Safe `0x91c3…d39b`.** Per EP6.2, the Meta-Gov Safe is the Allowance **delegate** (authorized to trigger the transfer), **not** the fee recipient ([Safe Tx Service](https://app.safe.global/)). Don't confuse the two when reconciling.

## Mechanics (no per-payment vote)

The fee runs through the Gnosis **Allowance Module** (`0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134`) installed on the **endowment Safe** (`endowment.ensdao.eth`, `0x4F2083…FE64`):

- **Standing allowance:** 30 ETH per period; `resetTimeMin` ≈ **25 days** (reduced from 30 by **EP6.2** to clear timing delays) ([Safe Tx Service](https://app.safe.global/)).
- **Payment call:** `executeAllowanceTransfer` — a MODULE_TRANSACTION, not a Safe owner tx. The allowance is authorized once, so no per-payment vote is needed ([Safe Tx Service](https://app.safe.global/)).
- **Observed:** 22 payments May 2024 → May 2026, ~monthly; min 12.74 / max 30.0 / mean ≈ 24.27 ETH ([Safe Tx Service](https://app.safe.global/)).

Addresses are canonical in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md).

## Monthly reconciliation

1. Pull the month's `executeAllowanceTransfer` ETH amount from the endowment Safe.
2. Confirm it is **within the 30 ETH cap** and consistent with 0.5%/yr against the reported **NAV** in that month's [Endowment Monthly Report](https://discuss.ens.domains/t/17614).
3. Confirm the destination was the fee Safe `0x58e6…`, not any other address.

> ⚠️ **Open question:** the on-chain **performance-fee** settlement pattern is unverified; treat the monthly Endowment Reports as authoritative for performance-fee amounts ([Endowment Monthly Reports, thread 17614](https://discuss.ens.domains/t/17614)).
