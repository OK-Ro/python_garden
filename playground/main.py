import random
import os

# Emojis for Rock, Paper, Scissors
emojis = {'r': '🪨', 'p': '📜', 's': '✂️'}
choices = ('r', 'p', 's')

# Scores
player_score = 0
computer_score = 0
ties = 0

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_scores():
    print(f"\n🏆 Scores:")
    print(f" You: {player_score} | Computer: {computer_score} | Ties: {ties}\n")

def print_separator():
    print("-" * 40)

# Welcome message
clear_screen()
print("🎮 Welcome to Rock-Paper-Scissors Arcade! 🎮")
print("Instructions: r = Rock, p = Paper, s = Scissors, q = Quit")

while True:
    print_separator()
    user_choice = input("Your move (r/p/s or q to quit): ").lower()

    if user_choice == 'q':
        print("Thanks for playing! 👋")
        print_scores()
        break

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    # Show moves
    print(f"\nYou chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
        ties += 1
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("💀 You lose this round!")
        computer_score += 1

    print_scores()