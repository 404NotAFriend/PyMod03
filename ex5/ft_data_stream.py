#!/usr/bin/env python3
import typing
import random


PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (name, action)


def main() -> None:
    generator = gen_event()
    print(next(generator))
    print(next(generator))
    print(next(generator))


if __name__ == "__main__":
    main()