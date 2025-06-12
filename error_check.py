# Assignment: Check your Knowledge on Errors
# Mandy Lubinski

# Task 1 - Understanding Python Exceptions
while True:
    # Prompts the user to enter a number.
    n = input("Enter a number: ")
    try: 
        n = float(n)
        # Tries to divide 100 by the number.
        result = 100 / n
    # ValueError (when the user enters non-numeric input).
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    # ZeroDivisionError (when dividing by zero).
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    else:
        print(f"100 divided by {n} is {result}")
        break

# Task 2 - Types of Exceptions
my_list = [1, 2, 3]
try:
    my_list[10]
# IndexError occurred because I tried to access an item in the list that does not exist (because by index, my_list has indices from 0-2)
except IndexError:
    print("IndexError occurred! List index out of range.")

my_dict = {"a": 1, "b": 2, "c": 3}
try:
    my_dict["z"]
# KeyError occurred because I tried to access a value in the dictionary that does not exist (because in my_dict the key "z" does not exist)
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    "Hello" + 5
# TypeError occurred because you cannot add a string and integer together
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

# Task 3 - Using try...except...else...finally
# Prompts the user to enter two numbers.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    # Tries to divide the first number by the second number.
    div_result = num1 / num2 
# Except block to handle exceptions
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
     print("You can't divide by zero!")
# Else block to display the result if no exceptions occur
else:
    print(f"The result is {div_result}.")
# Finally block to print a closing message regardless of exceptions
finally:
    print("Thank you for dividing two numbers today!")