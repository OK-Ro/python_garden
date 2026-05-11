import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(events: list) -> typing.Generator[tuple, None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events[index]
        del events[index]
        yield event


def main():
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for index in range(1000):
        name, action = next(stream)
        print(f"Event {index}: Player {name} did action {action}")

    stream = gen_event()
    event_list = []

    for _ in range(10):
        event_list.append(next(stream))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
