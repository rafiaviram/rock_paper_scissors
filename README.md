# rock_paper_scissors
In this implementation, we use the random.choice() function from the random module to get the computer's choice, and we define a play_round function to determine the winner of a single round of the game based on the player's choice and the computer's choice. We also define a play_game function to play multiple rounds of the game until the player chooses to stop.

To play a round of the game, we compare the player's choice to the computer's choice and determine the winner based on the following rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
We then print the choices and the winner.

To play the game, we get the player's choice using the input() function and check if it is valid. If it is, we play a round of the game using the play_round function, and ask the player if they want to play again using the input() function. If the player answers "yes", we play another round, and if they answer "no", we break out of the loop and end the game.
