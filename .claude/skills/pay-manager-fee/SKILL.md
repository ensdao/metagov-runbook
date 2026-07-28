---
name: pay-manager-fee
description: Use when paying karpatkey's monthly ENS endowment management fee, or when given an amount of ETH to send to the treasury manager and asked to prepare the Safe transaction.
---

# Pay the karpatkey management fee

Generate the Safe Transaction Builder batch that pays karpatkey's monthly management fee. The **input is the ETH amount** karpatkey specified for the month. The Meta-Gov Safe (Allowance Module delegate) calls `executeAllowanceTransfer`, moving that ETH from the Endowment Safe to karpatkey's fee Safe. The output is a proposal to import and sign in the Safe app; it never executes.

Run commands from the repo root.

## Steps

1. **Get the ETH amount** from the user (karpatkey's figure for the month).
2. **Sanity-check it.** It must be `<= 30` ETH (the per-period cap; the script rejects more). Recent monthly fees ran ~12.7 to 30 ETH (mean ~24). If the amount is far outside that range, confirm with the user before continuing.
3. **Generate the batch:**
   ```bash
   python3 scripts/manager_fee_to_safe.py --amount-eth <ETH> -o manager-fee.json
   ```
4. **Report and remind.** Give the output path and: import it in the Safe app (Transaction Builder then Load), and verify the amount and the fee-Safe destination in the UI before signing.

## Common mistakes

- Hand-building the calldata instead of using the script. The script mirrors the real on-chain call; hand-encoding is error-prone.
- Skipping the sanity check on an unusual amount.
- Treating the output as executed. It is only a proposal to sign in the Safe UI.

## Reference

- Mechanics and reconciliation: `04-runbook/treasury-manager-fees.md`
- The script and its flags: `scripts/README.md`
