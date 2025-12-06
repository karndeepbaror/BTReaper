#!/usr/bin/env python3

import argparse
from core import connect, BluezTarget, BluezAddressType


def main():
    parser = argparse.ArgumentParser(
        prog="Connect",
        description="Try To Connect To A Device Using System Tools",
    )
    parser.add_argument(
        "-a",
        "--target-address",
        help="Target Device MAC Address",
        required=True,
        dest="address",
    )
    parser.add_argument(
        "-t",
        "--target-address-type",
        help="Target Device MAC Address Type",
        dest="address_type",
        type=lambda t: BluezAddressType[t],
        choices=list(BluezAddressType),
        default=BluezAddressType.BR_EDR,
    )
    args = parser.parse_args()

    connect(BluezTarget(args.address, args.address_type), verbose=True)


if __name__ == "__main__":
    main()
