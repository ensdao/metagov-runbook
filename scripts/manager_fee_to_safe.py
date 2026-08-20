#!/usr/bin/env python3
"""Emit a Safe Transaction Builder batch JSON that pays the karpatkey management fee.

The Meta-Gov Safe is the Allowance Module delegate (per EP 6.2). It calls
`executeAllowanceTransfer` on the Allowance Module, which moves the monthly ETH fee
from the Endowment Safe to karpatkey's fee Safe. The amount is set by karpatkey each
month (0.5%/yr on NAV), capped at 30 ETH per period by the module.

This mirrors the real recurring transaction; import the output in the Safe web app
(Apps -> Transaction Builder -> Load) and verify every field before signing.

See 04-runbook/treasury-manager-fees.md.

Usage:
    python3 scripts/manager_fee_to_safe.py --amount-eth 24.42 [-o fee.json]
"""
import argparse
import sys
from decimal import Decimal, InvalidOperation

from safe_batch import build_batch, write

# Verified addresses. See ../02-contracts-and-multisigs/addresses.md
ALLOWANCE_MODULE = "0xCFbFaC74C26F8647cBDb8c5caf80BB5b32E43134"
ENDOWMENT_SAFE = "0x4F2083f5fBede34C2714aFfb3105539775f7FE64"
KPK_FEE_SAFE = "0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C"
META_GOV_SAFE = "0x91c32893216dE3eA0a55ABb9851f581d4503d39b"  # delegate
ETH = "0x0000000000000000000000000000000000000000"  # ETH sentinel in the Allowance Module
CAP_ETH = Decimal(30)  # per-period allowance cap


def fee_tx(amount_wei):
    return {
        "to": ALLOWANCE_MODULE,
        "value": "0",
        "data": None,
        "contractMethod": {
            "inputs": [
                {"internalType": "address", "name": "safe", "type": "address"},
                {"internalType": "address", "name": "token", "type": "address"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint96", "name": "amount", "type": "uint96"},
                {"internalType": "address", "name": "paymentToken", "type": "address"},
                {"internalType": "uint96", "name": "payment", "type": "uint96"},
                {"internalType": "address", "name": "delegate", "type": "address"},
                {"internalType": "bytes", "name": "signature", "type": "bytes"},
            ],
            "name": "executeAllowanceTransfer",
            "payable": False,
        },
        "contractInputsValues": {
            "safe": ENDOWMENT_SAFE,
            "token": ETH,
            "to": KPK_FEE_SAFE,
            "amount": str(amount_wei),
            "paymentToken": ETH,
            "payment": "0",
            "delegate": META_GOV_SAFE,
            "signature": "0x",
        },
    }


def main():
    ap = argparse.ArgumentParser(description="Pay the karpatkey management fee -> Safe batch JSON")
    ap.add_argument("--amount-eth", required=True,
                    help="fee amount in ETH (karpatkey's figure for the month)")
    ap.add_argument("-o", "--out", default="manager-fee.json", help="output JSON path")
    args = ap.parse_args()

    try:
        eth = Decimal(args.amount_eth)
    except InvalidOperation:
        sys.exit(f"invalid --amount-eth: {args.amount_eth!r}")
    if eth <= 0:
        sys.exit("--amount-eth must be positive")
    if eth > CAP_ETH:
        sys.exit(f"--amount-eth {eth} exceeds the {CAP_ETH} ETH per-period cap; the transfer would revert")

    wei = int(eth * (10 ** 18))
    desc = (f"Pay the karpatkey management fee: {eth} ETH from the Endowment Safe to the fee Safe, "
            f"via executeAllowanceTransfer on the Allowance Module. Confirm the amount matches "
            f"karpatkey's monthly figure before signing.")
    batch = build_batch(META_GOV_SAFE, "karpatkey management fee", desc, [fee_tx(wei)])
    write(args.out, batch)
    print(f"Wrote {args.out}: pay {eth} ETH ({wei} wei) to the fee Safe from the Endowment Safe.")
    print("Import in the Safe app (Transaction Builder -> Load) and verify every field before signing.")


if __name__ == "__main__":
    main()
