#rock paper scissors game

import random

def rockpapersci():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose: rock, paper, or scissors")

    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        pass
    else:
        print("Invalid choice. Please choose: rock, paper, or scissors")
        user_choice = input()
        user_choice = user_choice.lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")


rockpapersci()

