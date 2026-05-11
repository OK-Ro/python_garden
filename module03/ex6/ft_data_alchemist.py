import random


def main():
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    capitalized_players = [player.capitalize() for player in players]
    initial_capitalized_players = [player for player in players if player[0].isupper()]

    scores = {player: random.randint(1, 1000) for player in capitalized_players}
    average = sum(scores.values()) / len(scores)

    high_scores = {player: score for player, score in scores.items() if score > average}

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {initial_capitalized_players}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
