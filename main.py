#! /usr/bin/env python3
import random

# define function for the game


def game_result(user_choice, computer_choice):
    # Define the game rules
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "snake" and computer_choice == "water") or \
        (user_choice == "water" and computer_choice == "gun") or \
            (user_choice == "gun" and computer_choice == "snake"):
        return "You won!"
    else:
        return "You lost!"

# Define the main funtion


def snake_water_gun():
    print("Welcome to the Snake-Water-Gun game!")
    print("Rules: snake beats water, water beats gun, and gun beats snake")
    choices = ["snake", "water", "gun"]

    while True:
        user_choice = input(
            "Enter your choice (snake/water/gun or 'quit' to exit the game):  ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice! Please enter a valid choice")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        result = game_result(user_choice, computer_choice)
        print(result)
        print()


# Run the game by calling the main function
snake_water_gun()
