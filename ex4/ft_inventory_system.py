#!/usr/bin/env python3
import sys


def parse_inventory() -> dict[str, int]:

    arg_count: int = len(sys.argv)
    arguments: list[str] = sys.argv[1:]

    if arg_count < 2:
        return {}

    inventory: dict[str, int] = {}
    for arg in arguments:
        check_parts: list[str] = arg.split(":")
        if len(check_parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            item_name: str = check_parts[0].strip()
            try:
                quantity: int = int(check_parts[1])
                if item_name in inventory:
                    print(f"Redundant item '{item_name}' - discarding")
                else:
                    inventory[item_name] = quantity
            except ValueError as e:
                print(f"Quantity error for '{item_name}': {e}")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = parse_inventory()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")
    total: int = sum(inventory.values())
    for item_name in (inventory):
        percentage: float = round(
            (inventory[item_name] / total) * 100, 1)
        print(f"Item {item_name} represents {percentage}%")
    most_name: str = list(inventory.keys())[0]
    most_qty: int = inventory[most_name]
    for item_name in inventory:
        if inventory[item_name] > most_qty:
            most_qty = inventory[item_name]
            most_name = item_name
    print(f"Item most abundant: {most_name} with quantity {most_qty}")
    least_name: str = list(inventory.keys())[0]
    least_qty: int = inventory[least_name]
    for item_name in inventory:
        if inventory[item_name] < least_qty:
            least_qty = inventory[item_name]
            least_name = item_name
    print(f"Item least abundant: {least_name} with quantity {least_qty}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
