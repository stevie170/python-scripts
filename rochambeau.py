# a Python script to play the game rochambeau (rock, paper, scissors)
# user vs computer

import random

play = ["rock", "paper", "scissors"]

comp = random.choice(play)
player = False

# set base scores to 0
comp_score = 0
player_score = 0

# introduce the game
print("Let's play a game!")
print("Ever heard of Rochambeau?")
print("You might call it ""Rock, Paper, Scissors.""")
print("Enter your choice, or type ""end"" to stop the game.")


while True: # loop until the loop breaks
  player = input("rock, paper, or scissors? ").capitalize() # capitalize the input (first letter only) so it's easy to use in conditional statements
  
# a series of conditionals to see who won and keep score
  if player == comp
    print("You both chose ", comp, ". Tie!")
    elif player == "Rock":
      if comp == "Paper":
        print("You lose! ", comp, " covers ", player, ".")
        comp_score += 1  # add 1 to the computer's score
      else:
        print("You win! ", player, " smashes ", comp, ".")
        player_score += 1  # add 1 to the player's score
    elif player == "Paper":
      if comp == "Scissors":
        print("You lose! ", comp, " cut ", player, ".")
        comp_score += 1  # add 1 to the computer's score
      else:
        print("You win! ", player, " covers ", comp, ".")
        player_score += 1  # add 1 to the player's score
    elif player == "Scissors":
      if comp == "Rock":
        print("You lose! ", comp, " smashes ", player, ".")
        comp_score += 1  # add 1 to the computer's score
      else:
        print("You win! ", player, " cut ", comp, ".")
        player_score += 1  # add 1 to the player's score
    elif player == "End": # stop the game, print the score
      print("Final Scores: ")
      print(f"CPU:{comp_score}")
      print(f"Player:{player_score}")
      break # end the loop (note that this break is inside the conditional statement for if the player inputs "End."
