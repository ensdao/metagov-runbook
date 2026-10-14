# Treasury-Manager Fees (karpatkey)

karpatkey is paid two fees for managing the endowment. The **management fee** is automated and monthly; the **performance fee** is settled separately on realized yields ([endowment FAQ/initiation threads](https://discuss.ens.domains/)).

## Fee model

| Fee | Rate | Paid | Cap |
|---|---|---|---|
| Management | 0.5% / yr | **Monthly, in ETH** | ≤ **30 ETH / period** |
| Performance | 10% | Settled on realized yield, in the yield's reference currency | n/a |

Source: [endowment FAQ/initiation threads](https://discuss.ens.domains/).

## ⚠️ Where the fee lands: NOT the Meta-Gov Safe

The recurring management fee is paid **endowment Safe → the karpatkey fee Safe `0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C`** (verify against [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md)) ([Safe Tx Service](https://app.safe.global/)).

> **It does NOT land at the Meta-Gov Safe `0x91c3…d39b`.** Per EP6.2, the Meta-Gov Safe is the Allowance **delegate** (authorized to trigger the transfer), **not** the fee recipient ([Safe Tx Service](https://app.safe.global/)). Don't confuse the two when reconciling.

## Mechanics (no per-payment vote)

The fee runs through the Gnosis **Allowance Module** (`0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134`) installed on the **endowment Safe** (`endowment.ensdao.eth`, `0x4F2083…FE64`):

- **Standing allowance:** 30 ETH per period; `resetTimeMin` = 36,000 min = **25 days** (reduced from 30 by **EP6.2** to clear timing delays). Read on-chain 2026-10-14 with `getTokenAllowance(endowment, Meta-Gov Safe, ETH)` on the [module](https://etherscan.io/address/0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134#readContract).
- **Payment call:** `executeAllowanceTransfer`, a MODULE_TRANSACTION, not a Safe owner tx. The allowance is authorized once, so no per-payment vote is needed ([Safe Tx Service](https://app.safe.global/)).
- **Observed:** 22 payments May 2024 → May 2026, ~monthly; min 12.74 / max 30.0 / mean ≈ 24.27 ETH ([Safe Tx Service](https://app.safe.global/)).

Addresses are canonical in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md).

## Who triggers the fee (current state, _as of 2026-10-14_)

- The **Meta-Gov Safe is the only delegate** on the Allowance Module (`getDelegates` on the [module](https://etherscan.io/address/0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134#readContract), read 2026-10-14). The September 2026 fee (15.71 ETH) was triggered this way on 2026-10-07 ([MetaGov transaction index](https://discuss.ens.domains/t/22401)).
- The Endowment Safe's owner changed on 2026-08-11 (see [endowment-permissions.md](../03-treasury-and-endowment/endowment-permissions.md)). The fee allowance is an existing DAO-approved permission and continues unchanged ([Meta-Gov funding request](https://discuss.ens.domains/t/22475)).
- The Meta-Gov Term 7 funding request says the stewards trigger the fee "until the fee payout moves to the Foundation" ([forum](https://discuss.ens.domains/t/22475)). The Allowance Module keys delegates and allowances on the Safe that calls it (`msg.sender`, [source](https://github.com/safe-global/safe-modules/blob/main/modules/allowances/contracts/AllowanceModule.sol#L425)). So adding or removing a delegate is an Endowment Safe transaction, which the Foundation Safe schedules on the 9-day EndowmentTimelock.

> ⚠️ **Open question:** When and how the fee payout moves to the Foundation (new delegate address, whether the Meta-Gov Safe is removed, whether the 30 ETH / 25-day parameters change) → [OPEN-QUESTIONS Q-33](../OPEN-QUESTIONS.md). Until the module shows a change on-chain, keep running the monthly payment below.

## Generating the payment

Run [`scripts/manager_fee_to_safe.py`](../scripts/manager_fee_to_safe.py) `--amount-eth <karpatkey's figure for the month>` to emit the Safe Transaction Builder batch for the `executeAllowanceTransfer` call. Import it in the Safe app and verify every field (the amount, and the fee-Safe destination) before signing. The script rejects amounts above the 30 ETH cap.

## Monthly reconciliation

1. Pull the month's `executeAllowanceTransfer` ETH amount from the endowment Safe.
2. Confirm it is **within the 30 ETH cap** and consistent with 0.5%/yr against the reported **NAV** in that month's [Endowment Monthly Report](https://discuss.ens.domains/t/17614).
3. Confirm the destination was the fee Safe `0x58e6…`, not any other address.

> ⚠️ **Open question:** the on-chain **performance-fee** settlement pattern is unverified; treat the monthly Endowment Reports as authoritative for performance-fee amounts ([Endowment Monthly Reports, thread 17614](https://discuss.ens.domains/t/17614)).
