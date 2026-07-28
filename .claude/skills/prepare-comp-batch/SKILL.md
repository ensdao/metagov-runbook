---
name: prepare-comp-batch
description: Use when preparing the ENS Meta-Gov monthly steward or contributor USDC compensation payout, or building the recurring comp batch for the Safe.
---

# Prepare the monthly compensation batch

Build the Safe Transaction Builder batch for the monthly USDC compensation run. Anchor it on the **last actual payout** and **confirm the roster with the user** before generating anything. The output is a proposal to import and sign; it never executes.

Run commands from the repo root.

## Steps

1. **Pull the last compensation run.** Fetch the Meta-Gov Safe's most recent monthly USDC `multiSend` and decode its recipients and amounts:
   ```
   https://api.safe.global/tx-service/eth/api/v1/safes/0x91c32893216dE3eA0a55ABb9851f581d4503d39b/multisig-transactions/?limit=30&executed=true
   ```
   Find the newest `multiSend` of USDC transfers; list each recipient and amount (reverse-resolve ENS names where you can).
2. **Present it and confirm with the user.** Show the last roster and ask: is this the correct list for this run, or are there adds, removes, or amount changes? Wait for the answer.
3. **Verify recipients.** Every address must reverse-resolve to its expected ENS name (anti-phishing; see `04-runbook/verification-and-safety.md`). A mismatch stops the run.
4. **Write the confirmed roster to CSV** (`address,amount[,label]`) and generate the batch. Write the CSV and the output JSON to a scratch path outside the repo; payout data should not be committed.
   ```bash
   python3 scripts/usdc_batch_to_safe.py /path/to/roster.csv -o /path/to/usdc-batch.json
   ```
5. **Report** the output path and the diff versus last month. Remind: import in the Safe app and re-verify each row before signing.

## Confirmation gate

Do not generate the batch until BOTH are true: it is derived from the last actual payout (step 1), and the user has confirmed the roster (step 2). Never generate from an assumed or invented roster. If you cannot fetch the last payout, ask the user for the roster; do not guess it.

## Reference

- Full procedure: `04-runbook/monthly-compensation.md`
- The script and CSV format: `scripts/README.md`
