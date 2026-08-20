"""Helpers to emit Safe Transaction Builder batch JSON (mainnet).

The output is the batch-file format the Safe web app's **Transaction Builder**
loads via its Import / Load button. These helpers build PROPOSALS only; every
value must still be verified in the Safe UI before signing. See scripts/README.md.

Stdlib only (no dependencies). The `checksum` is left null: the Safe app
recomputes it on import.
"""
import json
import time

CHAIN_ID = "1"  # Ethereum mainnet


def erc20_transfer_tx(token, to, amount_base_units):
    """One ERC-20 transfer(to, value) transaction in Transaction Builder form."""
    return {
        "to": token,
        "value": "0",
        "data": None,
        "contractMethod": {
            "inputs": [
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
            ],
            "name": "transfer",
            "payable": False,
        },
        "contractInputsValues": {"to": to, "value": str(amount_base_units)},
    }


def build_batch(safe, name, description, transactions):
    """Wrap a list of transactions in the Transaction Builder batch file."""
    return {
        "version": "1.0",
        "chainId": CHAIN_ID,
        "createdAt": int(time.time() * 1000),
        "meta": {
            "name": name,
            "description": description,
            "txBuilderVersion": "1.17.1",
            "createdFromSafeAddress": safe,
            "createdFromOwnerAddress": "",
            "checksum": None,  # the Safe app recomputes this on import
        },
        "transactions": transactions,
    }


def write(path, batch):
    with open(path, "w") as f:
        json.dump(batch, f, indent=2)
        f.write("\n")
