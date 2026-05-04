#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    possible_achievements = [
        "Speed Runner", "Survivor", "Crafting Genius", "World Savior",
        "Master Explorer", "Treasure Hunter", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Strategist", "Unstoppable", "Hidden Path Finder"
    ]

    num_achievements = random.randint(4,9)
    chosen_achievements = random.sample(possible_achievements,
                                        num_achievements)
    
    return set(chosen_achievements)

def main () -> None:
    
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print("")
    all_achievements = alice.union(bob, charlie, dylan)
    print(f"All distict achievements: {all_achievements}")
    print("")

    print(f"Only")
    alice_unique = alice.difference()


if __name__ == "__main__":
    main()
    