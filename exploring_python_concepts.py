# Assignment: Exploring Python Concepts
# Mandy Lubinski

# Task 1 - Variables: Your First Python Intro
name = "Rameses"
age = 100
height = 2.83

print("Hi! My name is", name, "and I am the mascot for the best school in the world, UNC Chapel Hill. I have been UNC's mascot for", age, "years now and I'm about", height, "feet tall.")

# Task 2 - Operators: Playing with Numbers
num1 = 7
num2 = 4

print("The sum of 7 and 4 is", num1 + num2)
print("The difference of 7 and 4 is", num1 - num2)
print("The product of 7 and 4 is", num1 * num2)
print("The quotient of 7 and 4 is", num1 / num2)
# For each of these print statements, I included a statement saying I was going to end up with the end result of whatever operator I was performing on the two variables I previously named. 
# Then, using the previously initialized number variables, I used the corresponding arithmetic operator for each print statement.

# Task 3 - Conditional Statements: The Number Checker
x = float(input())

if x > 0:
    print("This number is positive. Awesome!")
elif x < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")