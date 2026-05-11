import random

ALL_POSSIBLE_ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


def gen_player_achievements():
    random_pick = random.randint(1, len(ALL_POSSIBLE_ACHIEVEMENTS))
    return set(random.sample(ALL_POSSIBLE_ACHIEVEMENTS, random_pick))


print("=== Achievement Tracker System ===\n")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

players = {"Alice": alice, "Bob": bob, "Charlie": charlie, "Dylan": dylan}

for name, achievements in players.items():
    print(f"Player {name}: {achievements}")
print()

# UNION
all_achievements = alice | bob | charlie | dylan
print("All distinct achievements:", all_achievements)
print()

# INTERSECTION
common_achievements = alice.intersection(bob, charlie, dylan)
print("Common achievements:", common_achievements)
print()

# UNIQUE per player
print("Only Alice has:", alice.difference(bob, charlie, dylan))
print("Only Bob has:", bob.difference(alice, charlie, dylan))
print("Only Charlie has:", charlie.difference(alice, bob, dylan))
print("Only Dylan has:", dylan.difference(alice, bob, charlie))
print()

# MISSING (IMPORTANT FIX: use MASTER LIST)
print("Alice is missing:", set(ALL_POSSIBLE_ACHIEVEMENTS) - alice)
print("Bob is missing:", set(ALL_POSSIBLE_ACHIEVEMENTS) - bob)
print("Charlie is missing:", set(ALL_POSSIBLE_ACHIEVEMENTS) - charlie)
print("Dylan is missing:", set(ALL_POSSIBLE_ACHIEVEMENTS) - dylan)