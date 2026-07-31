# Monthly Compensation Run

Contributors are paid in **USDC** roughly **monthly** (early in the month, ~1st–2nd) as a **single `multiSend` batch** out of the Meta-Gov main Safe to ~10 ENS-named recipients ([Safe Tx Service](https://app.safe.global/)).

> ⚠️ Read [verification-and-safety.md](verification-and-safety.md) first. The recipient list is exactly where address-poisoning attacks aim.

## Source of truth: the versioned roster

Maintain a **versioned recipient + amount roster** (e.g. JSON in the WG ops repo) as the single source for each run. Do not hand-type recipients into the Safe UI. Governance-set per-role rates live in [../05-terms/term-07.md](../05-terms/term-07.md); recurring per-person amounts observed on-chain include 9,500 / 5,500 / 4,000 / 3,000 USDC ([Safe Tx Service](https://app.safe.global/)).

## Procedure

1. **Update the roster.** Branch the previous month's roster; apply any agreed adds/removes/amount changes from the WG.
2. **Cross-check the current term.** The previous roster is only a valid starting point inside the same term. At a term boundary ([../05-terms/](../05-terms/README.md)) the steward set and roles turn over: rebuild the roster from the current term page's roster and per-role rates instead of carrying the old list forward. A recent `swapOwner`/`changeThreshold` on the Safe is the on-chain sign of that transition.
3. **Diff vs. last month.** Produce an explicit diff (added, removed, changed). Every delta must trace to a WG decision. An unexplained diff blocks the run.
4. **Verify each recipient ENS resolves.** Every address must reverse-resolve to its **expected** ENS name. A mismatch means a poisoned address slipped in. Stop.
5. **Generate the batch.** Convert the roster to a Safe **Transaction Builder** batch with [`scripts/usdc_batch_to_safe.py`](../scripts/usdc_batch_to_safe.py) (a CSV of `address,amount` becomes one importable JSON) so all signers review one batch, not N transfers.
6. **Confirm the token.** The asset must be canonical USDC (see [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md)), never a homoglyph "USDС".
7. **Cross-check decoded calldata.** Recipient count and per-recipient amounts in the decoded batch must equal the roster. Confirm the **sum** matches the expected batch total.
8. **Collect signatures and execute.** Meet the main Safe threshold in [addresses.md](../02-contracts-and-multisigs/addresses.md) ([Safe Tx Service](https://app.safe.global/)). Each signer independently re-runs steps 4 and 7 before approving.

## After execution

- Archive the exact roster version used alongside the executed Safe tx hash for auditability.
- Confirm the runway can cover the next run; see [funding-request.md](funding-request.md).

## Notes

- Funding for this spend comes from per-term DAO→Safe USDC top-ups → [funding-request.md](funding-request.md).
- Compensation amounts and roster changes are a WG governance matter; this page covers only the **execution** mechanics.
