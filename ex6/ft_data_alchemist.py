#!/usr/bin/env python3
import random

PLAYERS: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                      "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {PLAYERS}")
    all_cap: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {all_cap}")
    only_cap: list[str] = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")
    print()

    score: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_cap
    }
    print(f"Score dict: {score}")
    average_score: float = round(sum(score.values()) / len(score), 2)
    print(f"Score average is {average_score}")
    high_scores: dict[str, int] = {
        name: points
        for name, points in score.items()
        if points > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
