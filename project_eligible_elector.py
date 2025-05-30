# Project: Eligible Elector
# Mandy Lubinski

# First, I created an age variable for the user to input their age. I also changed the variable type to an integer (as opposed to a string).
age = int(input("How old are you? "))

# This is my if else statement. My if statement is if the age is greater than or equal to 18 and my else statement is if the age is less than 18.
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You’re not eligible yet. But hey, only", 18 - age, "more years to go!")


