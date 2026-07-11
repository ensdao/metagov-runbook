# Token Distribution (Hedgey Vesting)

ENS token distributions (e.g. the token-distribution program under EP5.26) are funded as **Hedgey vesting plans**, created in a **two-step** batch from the Meta-Gov Safe ([Safe Tx Service](https://app.safe.global/)). ~233k ENS has been routed this way over the program's lifetime ([Safe Tx Service](https://app.safe.global/)).

> ⚠️ Read [verification-and-safety.md](verification-and-safety.md) first.

## The two-step template

1. **`approve(ENS)`.** Approve the ENS token spend to the **Hedgey BatchPlanner** (`0x3466EB008EDD8d5052446293D1a7D212cb65C646`, verify against [addresses.md](../02-contracts-and-multisigs/addresses.md)).
2. **`batchVestingPlans`.** Call BatchPlanner with the array of recipient plans.

Both steps go in one Safe **Transaction Builder** batch so signers review them together ([Safe Tx Service](https://app.safe.global/)). The BatchPlanner address and the ENS token are in [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md). Verify both there.

## Mandatory pre-sign checks

- **`approve` total == sum of plan amounts.** Add up every plan's amount in the `batchVestingPlans` array; it must equal the `approve` value **exactly**. An approve larger than the plan sum leaves a standing allowance. Do not sign.
- **Spender is the canonical BatchPlanner.** Confirm step 1 approves `0x3466EB…C646`, not a lookalike.
- **Each recipient resolves to its expected ENS name** and matches the governing EP's recipient list.
- **Total matches the EP.** The aggregate distributed must equal the amount the governing EP authorized.
- **Decoded calldata reviewed.** Read the decoded batch in the Transaction Builder before approving.

## Link the governing EP

Every tranche must trace to the EP that authorized it (e.g. EP5.26). Record the EP number, the approved amount, and the executed Safe tx hash together. See [../reference/governance-history.md](../reference/governance-history.md).

## Execution

Collect the main Safe signatures per its threshold in [addresses.md](../02-contracts-and-multisigs/addresses.md) and execute ([Safe Tx Service](https://app.safe.global/)). Each signer independently re-verifies the approve-equals-sum check before approving.
