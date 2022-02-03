#!/usr/bin/env python3

# a Python script to play the game rochambeau (rock, paper, scissors)
# user vs computer

import random

# set base scores to 0
computer_score = 0
player_score = 0

# introduce the game
print("\n")
print("Let's play a game!")
print("Ever heard of Rochambeau?")
print("You might call it \"Rock, Paper, Scissors.\"")
print("Enter your choice, or type \"end\" to stop the game.")
print("\n")

choices = ['Rock', 'Paper', 'Scissors']

while True: # loop until the loop breaks
  computer = random.choice(choices)
  player = input("rock, paper, or scissors? ").capitalize() # capitalize the input (first letter only) so it's easy to use in conditional statements
  
# a series of conditionals to see who won and keep score
  if player == computer:
    print("Tie! You both chose", computer)
  elif player == "Rock":
    if computer == "Paper":
      print("You lose! ", computer, "covers", player)
      computer_score += 1  # add 1 to the computer's score
    else:
      print("You win! ", player, "smashes", computer)
      player_score += 1  # add 1 to the player's score
  elif player == "Paper":
    if computer == "Scissors":
      print("You lose! ", computer, "cut", player)
      computer_score += 1  # add 1 to the computer's score
    else:
      print("You win! ", player, "covers", computer)
      player_score += 1  # add 1 to the player's score
  elif player == "Scissors":
    if computer == "Rock":
      print("You lose! ", computer, "smashes", player)
      computer_score += 1  # add 1 to the computer's score
    else:
      print("You win! ", player, "cut", computer)
      player_score += 1  # add 1 to the player's score
  elif player == "End": # stop the game, print the score
    print("Final Scores:")
    print(f"CPU: {computer_score}")
    print(f"Player: {player_score}")
    break # end the loop (note that this break is inside the conditional statement for if the player inputs "End."
  else: # stop the game, error
    print("Invalid input. Hope you'll try again!") # can I use a while loop to prompt for a valid input instead? Kind of like how I did with the password generator? Hmmm...
    break # end the loop (note that this break is inside the conditional statement for if the player enters invalid input.

