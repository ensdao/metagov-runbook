#!/usr/bin/env python3
"""Convert a CSV of (address, USDC amount) into a Safe Transaction Builder batch JSON.

Each CSV row becomes one USDC transfer from the Meta-Gov Safe. Import the output in
the Safe web app (Apps -> Transaction Builder -> Load), then verify every recipient
and amount in the UI before signing.

See 04-runbook/monthly-compensation.md and 04-runbook/verification-and-safety.md.

CSV format: a header row with columns `address` and `amount` (USDC, decimal). An
optional `label` column is ignored by the encoder (use it for your own review).

    address,amount,label
    0xAbc...,9500,steward-a
    0xDef...,4000.50,contributor-b

Usage:
    python3 scripts/usdc_batch_to_safe.py roster.csv -o batch.json [--safe 0x...]
"""
import argparse
import csv
import re
import sys
from decimal import Decimal, InvalidOperation

from safe_batch import build_batch, erc20_transfer_tx, write

# mainnet USDC (6 decimals) and the Meta-Gov Safe. See ../02-contracts-and-multisigs/addresses.md
USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
META_GOV_SAFE = "0x91c32893216dE3eA0a55ABb9851f581d4503d39b"  # main.mg.wg.ens.eth
USDC_DECIMALS = 6
ADDR = re.compile(r"^0x[0-9a-fA-F]{40}$")


def main():
    ap = argparse.ArgumentParser(description="CSV -> Safe USDC transfer batch JSON")
    ap.add_argument("csv", help="input CSV with columns: address, amount [, label]")
    ap.add_argument("-o", "--out", default="usdc-batch.json", help="output JSON path")
    ap.add_argument("--safe", default=META_GOV_SAFE,
                    help="Safe that will execute (default: Meta-Gov Safe)")
    args = ap.parse_args()

    if not ADDR.match(args.safe):
        sys.exit(f"--safe is not a valid address: {args.safe!r}")

    txs, total, errors, seen = [], Decimal(0), [], set()
    with open(args.csv, newline="") as f:
        reader = csv.DictReader(f)
        cols = {c.lower().strip(): c for c in (reader.fieldnames or [])}
        if "address" not in cols or "amount" not in cols:
            sys.exit("CSV must have 'address' and 'amount' columns")
        for i, row in enumerate(reader, start=2):  # row 1 is the header
            addr = (row[cols["address"]] or "").strip()
            raw = (row[cols["amount"]] or "").strip()
            if not addr and not raw:
                continue  # tolerate blank lines
            if not ADDR.match(addr):
                errors.append(f"row {i}: invalid address {addr!r}")
                continue
            if addr.lower() in seen:
                errors.append(f"row {i}: duplicate address {addr}")
                continue
            try:
                amt = Decimal(raw)
            except InvalidOperation:
                errors.append(f"row {i}: invalid amount {raw!r}")
                continue
            if amt <= 0:
                errors.append(f"row {i}: amount must be positive ({raw})")
                continue
            base = int(amt * (10 ** USDC_DECIMALS))
            if amt * (10 ** USDC_DECIMALS) != base:
                errors.append(f"row {i}: amount {raw} has more than {USDC_DECIMALS} decimals")
                continue
            seen.add(addr.lower())
            txs.append(erc20_transfer_tx(USDC, addr, base))
            total += amt

    if errors:
        sys.exit("CSV errors (nothing written):\n  " + "\n  ".join(errors))
    if not txs:
        sys.exit("no valid rows found")

    desc = (f"{len(txs)} USDC transfers, total {total} USDC. "
            f"Verify every recipient and amount in the Safe UI before signing.")
    batch = build_batch(args.safe, "USDC batch payout", desc, txs)
    write(args.out, batch)
    print(f"Wrote {args.out}: {len(txs)} USDC transfers, total {total} USDC, from Safe {args.safe}.")
    print("Import in the Safe app (Transaction Builder -> Load) and verify each row before signing.")


if __name__ == "__main__":
    main()
