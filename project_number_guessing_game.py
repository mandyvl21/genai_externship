# Project: Number Guessing Game
# Mandy Lubinski

# Step 1: Generate a Random Number
import random
number_to_guess = random.randint(1, 100)

# Steps 2, 3, and bonus task
count = 0 # starts the number of guesses count 
while count < 10: # limits number of guesses to 10
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess > number_to_guess: # if the guess was too high 
        print("Too high! Try again.")
    elif guess < number_to_guess: # if the guess was too low 
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {count + 1} attempts!") # if the user guesses the number correctly 
    count += 1
print(f"Game over! Better luck next time! The correct answer was {number_to_guess}.") # if the user uses all 10 attempts and doesn't guess the number