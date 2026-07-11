# Monthly Compensation Run

Contributors are paid in **USDC** roughly **monthly** (early in the month, ~1st–2nd) as a **single `multiSend` batch** out of the Meta-Gov main Safe to ~10 ENS-named recipients ([Safe Tx Service](https://app.safe.global/)).

> ⚠️ Read [verification-and-safety.md](verification-and-safety.md) first. The recipient list is exactly where address-poisoning attacks aim.

## Source of truth: the versioned roster

Maintain a **versioned recipient + amount roster** (e.g. JSON in the WG ops repo) as the single source for each run. Do not hand-type recipients into the Safe UI. Governance-set per-role rates live in [../05-terms/term-07.md](../05-terms/term-07.md); recurring per-person amounts observed on-chain include 9,500 / 5,500 / 4,000 / 3,000 USDC ([Safe Tx Service](https://app.safe.global/)).

## Procedure

1. **Update the roster** — branch the previous month's roster; apply any agreed adds/removes/amount changes from the WG.
2. **Diff vs. last month** — produce an explicit diff (added, removed, changed). Every delta must trace to a WG decision. An unexplained diff blocks the run.
3. **Verify each recipient ENS resolves** — every address must reverse-resolve to its **expected** ENS name. A mismatch means a poisoned address slipped in — stop.
4. **Generate the batch** — build the Safe **Transaction Builder** `multiSend` from the roster so all signers review one batch, not N transfers.
5. **Confirm the token** — the asset must be canonical USDC (see [../02-contracts-and-multisigs/addresses.md](../02-contracts-and-multisigs/addresses.md)), never a homoglyph "USDС".
6. **Cross-check decoded calldata** — recipient count and per-recipient amounts in the decoded batch must equal the roster. Confirm the **sum** matches the expected batch total.
7. **Collect signatures and execute** — meet the main Safe threshold in [addresses.md](../02-contracts-and-multisigs/addresses.md) ([Safe Tx Service](https://app.safe.global/)). Each signer independently re-runs steps 3 and 6 before approving.

## After execution

- Archive the exact roster version used alongside the executed Safe tx hash for auditability.
- Confirm the runway can cover the next run; see [funding-request.md](funding-request.md).

## Notes

- Funding for this spend comes from per-term DAO→Safe USDC top-ups → [funding-request.md](funding-request.md).
- Compensation amounts and roster changes are a WG governance matter; this page covers only the **execution** mechanics.
