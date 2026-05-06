#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    possible_achievements: list[str] = [
        "Speed Runner", "Survivor", "Crafting Genius", "World Savior",
        "Master Explorer", "Treasure Hunter", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Strategist", "Unstoppable", "Hidden Path Finder"
    ]

    num_achievements: int = random.randint(4, 9)
    chosen_achievements: list[str] = random.sample(possible_achievements,
                                                   num_achievements)

    return set(chosen_achievements)


def main() -> None:

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()
    all_achievements: set[str] = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}")
    print()

    common_achievements: set[str] = all_achievements.intersection(
        alice, charlie, bob, dylan)
    print(f"Common achievements: {common_achievements}")
    print()

    alice_unique: set[str] = alice.difference(bob, charlie, dylan)
    bob_unique: set[str] = bob.difference(alice, charlie, dylan)
    charlie_unique: set[str] = charlie.difference(alice, bob, dylan)
    dylan_unique: set[str] = dylan.difference(alice, bob, charlie)
    print(f"Only Alice has: {alice_unique}")
    print(f"Only Bob has: {bob_unique}")
    print(f"Only Charlie has: {charlie_unique}")
    print(f"Only Dylan has: {dylan_unique}")
    print()

    alice_missing: set[str] = all_achievements.difference(alice)
    print(f"Alice is missing: {alice_missing}")
    bob_missing: set[str] = all_achievements.difference(bob)
    print(f"Bob is missing: {bob_missing}")
    charlie_missing: set[str] = all_achievements.difference(charlie)
    print(f"Charlie is missing: {charlie_missing}")
    dylan_missing: set[str] = all_achievements.difference(dylan)
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
