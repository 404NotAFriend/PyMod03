#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    arg_count = len(sys.argv)
    args_only = sys.argv[1:]
    name = sys.argv[0]

    print("=== Command Quest ===")
    print(f"Program name: {name}")

    if arg_count == 1:
        print("No arguments provided!")
        print(f"Total arguments: {arg_count}")
    else:
        print(f"Arguments received: {len(args_only)}")
        for i in range(1, arg_count):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total Arguments: {arg_count}")


if __name__ == "__main__":
    ft_command_quest()
