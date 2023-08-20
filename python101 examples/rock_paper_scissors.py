import random

def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "rock" and computer_choice == "scissors"):
        return "player"
    else:
        return "computer"

choices = ["rock", "paper", "scissors"]

print("\n-----Rock-Paper-Scissors Game-----\n")
print("Enter 'exit' to quit")

player_score = 0
computer_score = 0

while True:
    player_choice = input("Enter your choice : ").lower()
    
    if player_choice == "exit":
        break
    
    if player_choice not in choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue
    
    computer_choice = random.choice(choices)
    
    print(f"Computer chose: {computer_choice.capitalize()}")
    winner = decide_winner(player_choice, computer_choice)
    
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    
    if winner == "tie":
        print("It's a tie! Play game for the tie break!")
    else:
        print(f"{winner.capitalize()} wins the game!")
    
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)

print("Game closed")
