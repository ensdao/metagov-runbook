# Scripts

Helper scripts for the runbook. All are Python 3, stdlib only (no dependencies).

| Script | Purpose |
| --- | --- |
| [`usdc_batch_to_safe.py`](usdc_batch_to_safe.py) | Convert a CSV of `address,amount` into a Safe batch JSON of USDC transfers |
| [`manager_fee_to_safe.py`](manager_fee_to_safe.py) | Build a Safe batch JSON that pays the karpatkey management fee |
| [`safe_batch.py`](safe_batch.py) | Shared helper that emits the Safe Transaction Builder batch format |
| [`verify.py`](verify.py) | Docs check (links, placeholders, address consistency); runs in CI |

## Safe Transaction Builder format

Both transaction scripts emit the **Transaction Builder** batch file. To use it:

1. Open the Safe web app for the [Meta-Gov Safe](../02-contracts-and-multisigs/addresses.md) → **Apps → Transaction Builder**.
2. **Load** the generated `.json`.
3. **Verify every transaction in the UI** (recipient, token, amount) against your source before proposing and signing. See [verification & safety](../04-runbook/verification-and-safety.md).

The scripts only build a proposal. They never sign or execute. The `checksum` field is left null; the Safe app recomputes it on import.

## `usdc_batch_to_safe.py`

```bash
python3 scripts/usdc_batch_to_safe.py roster.csv -o batch.json
```

CSV: a header row with `address` and `amount` (USDC, decimal); an optional `label` column is ignored by the encoder. See [`examples/usdc-batch.example.csv`](examples/usdc-batch.example.csv). Each row becomes one USDC transfer from the Meta-Gov Safe (override with `--safe`). The script rejects invalid or duplicate addresses, non-positive amounts, and amounts finer than USDC's 6 decimals, and writes nothing if any row is bad. Used by the [monthly compensation run](../04-runbook/monthly-compensation.md).

## `manager_fee_to_safe.py`

```bash
python3 scripts/manager_fee_to_safe.py --amount-eth 24.42 -o fee.json
```

Builds the one-transaction batch in which the Meta-Gov Safe (the Allowance Module delegate) calls `executeAllowanceTransfer`, moving that month's ETH fee from the Endowment Safe to karpatkey's fee Safe. `--amount-eth` is karpatkey's figure for the month; the script rejects amounts above the 30 ETH per-period cap. Used by [treasury-manager fees](../04-runbook/treasury-manager-fees.md).
