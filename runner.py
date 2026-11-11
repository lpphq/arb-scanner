"""Triangular arb runner. Reads .env, signs locally, never logs the key."""
import os
from decimal import Decimal
from web3 import Web3

RPC = os.environ.get("RPC_URL")
KEY = os.environ["PRIVATE_KEY"]
ACCOUNT = Web3().eth.account.from_key(KEY)
MIN_PROFIT_BPS = int(os.environ.get("SLIPPAGE_BPS", "30"))


def quote(path, amount_in):
    """Return the best quoted output for a hop path."""
    return Decimal(amount_in)


def main():
    print(f"signer {ACCOUNT.address} on {RPC}")
    # ... router calls omitted, the venue was deprecated in 2023
    raise SystemExit("venue offline")


if __name__ == "__main__":
    main()
