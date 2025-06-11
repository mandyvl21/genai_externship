# Project: About Menu
# Mandy Lubinski

# Importing turtle library
import turtle 

# Forcing turtle screen to open 
screen = turtle.Screen()  
screen.setup(width=800, height=600)

# Steps 1-4: Recursive functions

# Step 1: Menu of Recursive Functions
def menu():
    # Input for user to see useful information to run the program
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("> ")

        # uses get_positive_integer function to check that input is a positive integer before running factorial function
        if choice == "1":
            n = get_positive_integer("Enter a number to find its factorial: ")
            print(f"The factorial of {n} is {factorial(n)}.")

        # uses get_positive_integer function to check that input is a positive integer before running fibonacci function
        elif choice == "2":
            n = get_positive_integer("Enter the position of the Fibonacci number: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

        # runs fractal function 
        elif choice == "3":
            print("Drawing Koch snowflake fractal...")
            turtle.speed(0)
            turtle.penup()
            turtle.goto(-150, 90)
            turtle.pendown()
            for _ in range(3):
                fractal(300, 4)
                turtle.right(120)

            # to quit the turtle program and return to main menu
            input("Press Enter to return to the menu...")

        # to quit the program 
        elif choice == "4":
            print("Goodbye!")
            break

        # to ensure that the user inputs a valid number for the program to run
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")

# Step 2: Factorial Function
# Implement a recursive function to calculate the factorial of a number and display the result.
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1) 

# Step 3: Fibonacci Function
# Implement a recursive function to calculate the nth Fibonacci number and display the result.
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Step 4: Recursive Fractal Pattern 
# Using the turtle library, create a recursive function to draw a fractal pattern (e.g., a tree or snowflake).
def fractal(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        fractal(length, level - 1)
        turtle.left(60)
        fractal(length, level - 1)
        turtle.right(120)
        fractal(length, level - 1)
        turtle.left(60)
        fractal(length, level - 1)

# Step 5: User-Friendly Program
# Validate integer input (ensures positive integers only)
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Runs the program
menu()