---
name: prepare-comp-batch
description: Use when preparing the ENS Meta-Gov monthly steward or contributor USDC compensation payout, or building the recurring comp batch for the Safe.
---

# Prepare the monthly compensation batch

Build the Safe Transaction Builder batch for the monthly USDC compensation run. Anchor it on the **last actual payout** cross-checked against the **current term's roster**, and **confirm with the user** before generating anything. The output is a proposal to import and sign; it never executes.

Run commands from the repo root.

## Steps

1. **Pull the last compensation run.** Fetch the Meta-Gov Safe's most recent monthly USDC `multiSend` and decode its recipients and amounts:
   ```
   https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/multisig-transactions/?limit=30&executed=true
   ```
   Find the newest `multiSend` of USDC transfers; list each recipient and amount (reverse-resolve ENS names where you can).
2. **Anchor on the current term.** Read the newest `05-terms/term-NN.md` for the term dates, steward roster, and per-role rates. The last payout is only a valid template if it falls inside the current term:
   - If the last payout executed in a **previous term**, the roster has turned over: rebuild it from the term page — one row per role-holder at that role's rate — instead of carrying the old list forward.
   - Scan the transactions fetched in step 1 for `swapOwner` / `addOwner` / `removeOwner` / `changeThreshold`. An owner rotation near a term boundary is the on-chain signature of a steward transition; reverse-resolve the new owners (stewards use `steward.<name>.eth` subnames) to get candidate payment addresses.
   - Roles the term page leaves unappointed (e.g. Secretary, Scribe) are a question for the user, not a carry-over.
3. **Present the derived roster and confirm with the user.** Show the roster from steps 1–2 with an explicit diff versus the last payout, citing the term page for each rate. Ask: correct list for this run, or are there adds, removes, or amount changes? Wait for the answer.
4. **Verify recipients.** Every address must reverse-resolve to its expected ENS name (anti-phishing; see `04-runbook/verification-and-safety.md`). A mismatch stops the run.
5. **Write the confirmed roster to CSV** (`address,amount[,label]`) and generate the batch. Write the CSV and the output JSON to a scratch path outside the repo; payout data should not be committed.
   ```bash
   python3 scripts/usdc_batch_to_safe.py /path/to/roster.csv -o /path/to/usdc-batch.json
   ```
6. **Report** the output path and the diff versus last month. Remind: import in the Safe app and re-verify each row before signing.

## Confirmation gate

Do not generate the batch until ALL are true: it is derived from the last actual payout (step 1), cross-checked against the current term's roster (step 2), and the user has confirmed the roster (step 3). Never generate from an assumed or invented roster. If you cannot fetch the last payout, ask the user for the roster; do not guess it.

## Reference

- Current term roster and rates: newest `term-NN.md` in `05-terms/`
- Full procedure: `04-runbook/monthly-compensation.md`
- The script and CSV format: `scripts/README.md`
