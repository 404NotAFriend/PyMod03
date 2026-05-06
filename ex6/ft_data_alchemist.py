#!/usr/bin/env python3

PLAYERS: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                      "Gregory", "john", "kevin", "Liam"]


#list comprehensions 

def main() -> None:
    print(f"Initial list of players: {PLAYERS}")
    print()
    all_cap: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {all_cap}")
    print()
    only_cap: list[str] = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

if __name__ == "__main__":
    main()