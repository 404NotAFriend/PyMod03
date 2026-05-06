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


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        chosen: tuple[str, str] = random.choice(events)
        events.remove(chosen)
        yield chosen


def main() -> None:
    generator = gen_event()
    events: list[tuple[str, str]] = []
    for i in range(1000):
        event: tuple[str, str] = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    for i in range(10):
        event_lst: tuple[str, str] = next(generator)
        events = events + [event_lst]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: ('{event[0]}', '{event[1]}')")
        print(f"Remains on list: {events}")


if __name__ == "__main__":
    main()
