import random

# Define a list of the possible choices
choices = ["rock", "paper", "scissors"]

# Define a function to play a round of the game
def play_round(player_choice):
    # Get the computer's choice
    computer_choice = random.choice(choices)
    
    # Print the choices
    print(f"Player chooses {player_choice}, computer chooses {computer_choice}.")
    
    # Determine the winner
    if player_choice == computer_choice:
        print("Tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") \
         or (player_choice == "paper" and computer_choice == "rock") \
         or (player_choice == "scissors" and computer_choice == "paper"):
        print("Player wins!")
    else:
        print("Computer wins!")

# Define a function to play the game
def play_game():
    print("Let's play rock, paper, scissors!")
    while True:
        # Get the player's choice
        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        
        # Check if the input is valid
        if player_choice not in choices:
            print("Invalid choice, please try again.")
        else:
            # Play a round of the game
            play_round(player_choice)
            
            # Ask if the player wants to play again
            play_again = input("Do you want to play again? (yes or no): ")
            if play_again.lower() != "yes":
                break
    print("Thanks for playing!")

# Call the play_game function to start the game
play_game()
