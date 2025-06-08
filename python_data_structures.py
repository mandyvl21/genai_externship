# Assignment: Hands on Python Data Structures 
# Mandy Lubinski

# Task 1 - Working with Lists
# Create a list of your favorite fruits. Add at least five fruits to the list.
fruit = ["watermelon", "lychee", "mango", "strawberry", "dragonfruit"]
print(f"Original list: {fruit}")

# Append a new fruit to the list.
fruit.append("cherry")
print(f"After adding a fruit: {fruit}")

# Remove one fruit from the list using the remove() method.
fruit.remove("watermelon")
print(f"After removing a fruit: {fruit}")

# Print the list in reverse order using slicing.
print(f"Reversed list: {fruit[::-1]}")

# Task 2 - Exploring Dictionaries
# Create a dictionary to store information about yourself with the following keys: "name", "age", "city".
myself = {"name": "Mandy", "age": 20, "city": "Charlotte"}

# Add a new key-value pair to the dictionary for "favorite color".
myself["favorite color"] = "lavender"

# Update the "city" key with a new value.
myself["city"] = "Chapel Hill"

# Print all the keys and values using a loop.
key_list = []
for key in myself:
    key_list.append(key)
print(f"Keys: {key_list}")

value_list = []
for value in myself.values():
    value_list.append(value)
print(f"Values: {value_list}")

# Task 3 - Using Tuples
# Create a tuple with three elements: your favorite movie, song, and book.
fav_things = ("Perks of Being a Wallflower", "Kids", "Girl in Pieces")
print(f"Favorite things: {fav_things}")

# Try to change one of the elements (you’ll see why tuples are immutable!).
fav_things.append("lavender")

# Print the length of the tuple using the len() function.
print(f"Length of tuple: {len(fav_things)}")
