# Assignment: Explore Loops in Python
# Mandy Lubinski


# Task 1 - Counting Down with Loops
x1 = int(input("Enter the starting number: "))

while x1 > 1:
    print(x1)
    x1 -= 1 # changes condition and prevents infinite loop 
print("1 Blast off! 🚀")

# Task 2 - Multiplication Table with for Loops
x2 = int(input("Enter a number: "))

for num in range(1, 11): # range must go to num + 1
    print(f"{x2} x {num} = {x2 * num}")

# Task 3 - Find the Factorial
x3 = int(input("Enter a number: "))

factorial = 1 # first, create factorial (result) variable 
for i in range(1, x3 + 1): # range must go to x3 + 1
    factorial *= i # calculates factorial 
print(f"The factorial of {x3} is {factorial}.")
