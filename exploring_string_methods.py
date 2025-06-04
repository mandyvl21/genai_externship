# Assignment: Exploring String Methods
# Mandy Lubinski

# Task 1 - String Slicing and Indexing
x1 = "Python is amazing!" # Create a string variable with the value "Python is amazing!".

first_6 = x1[0:6]
print(f"First word: {first_6}") # The first 6 characters ("Python")

amazing = x1[10:17]
print(f"Amazing part: {amazing}") # The word "amazing"

reverse_order = x1[::-1]
print(f"Reversed string: {reverse_order}") # The entire string in reverse order

# Task 2 - String Methods
x2 = " hello, python world! " # Create a string with the value " hello, python world! ".

rm_ex_space = x2.strip()
print(rm_ex_space) # strip() to remove extra spaces

cap_first_letter = rm_ex_space.capitalize() # when using capitalize() with the original x2 string it did not work, I had to use the stripped version instead
print(cap_first_letter) # capitalize() to capitalize the first letter

replace_w_universe = x2.replace("world", "universe")
print(replace_w_universe) # replace() to replace "world" with "universe"

uppercase = x2.upper()
print(uppercase) # upper() to convert the string to uppercase



# Task 3 - Check for Palindromes
word = str(input("Enter a word: ")) # Ask the user to input a word.

reverse_word = word[::-1] # Use slicing to reverse the string and compare it with the original.

if word == reverse_word:
    print(f"Yes, \'{word}\' is a palindrome!") # Print a friendly message indicating whether the word is a palindrome.
else:
    print(f"Sorry, \'{word}\' is not a palindrome.") # Message that the word is not a palindrome. 