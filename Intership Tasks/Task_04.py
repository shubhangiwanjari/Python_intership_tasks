import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("🎮 Welcome to Rock, Paper, Scissors Game! 🎮")
    print("Type 'quit' anytime to exit.\n")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice == "quit":
            print("\nThanks for playing! Final Scores:")
            print(f"User: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

# Run the game
play_game()
