# Assignment: About Parameters of Functions
# Mandy Lubinski

# Task 1 - Writing Functions
# Create a function greet_user that accepts a name as a parameter and prints a personalized greeting.
def greet_user(name):
    print(f"Hello, nice to meet you, {name}!")

# Then, write another function add_numbers that takes two numbers as parameters, adds them, and returns the result.
def add_numbers(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1 + num2}.")

# Task 2 - Using Default Parameters
# Create a function describe_pet that accepts two parameters:
    # pet_name (string)
    # animal_type (string, default value is "dog").
    # The function should print a description of the pet.
def describe_pet(pet_name, animal_type = "dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Task 3 - Functions with Variable Arguments
# Write a function make_sandwich that accepts a variable number of arguments for sandwich ingredients and prints them as a list.
def make_sandwich(*args):
    print(f"Making a sandwich with the following ingredients: {' - '.join(str(arg) for arg in args)}")

# Task 4 - Understanding Recursion
# Write a recursive function factorial to calculate the factorial of a number.
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Then, write another recursive function fibonacci to calculate the nth number in the Fibonacci sequence.
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
