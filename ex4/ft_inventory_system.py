#!/usr/bin/env python3
import sys


def parse_inventory() -> dict[str, int]:

    arg_count: int = len(sys.argv)
    arguments: list[str] = sys.argv[1:]

    if arg_count < 2:
        return

    inventory: dict[str, int] = {}

    for arg in arguments:
        check_parts: list[str] = arg.split(":")
        if len(check_parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            try:
                item_name: str = check_parts[0].strip()
                quantity: int = int(check_parts[1])
                inventory.item_name = check_parts[0]
                inventory.quantity = check_parts[1]
            except ValueError as e:
                print(f"Quantity error for '{item_name}': {e}")


