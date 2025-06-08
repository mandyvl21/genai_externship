# Project: Implement Your own Data Structures
# Mandy Lubinski

# Step 1: Create the Inventory
print("Welcome to the Inventory Manager!")
inventory = {}

inventory["lychee"] = (30, 5)
inventory["watermelon"] = (10, 3)

print("Current inventory: ")
for key, value in inventory.items():
    print(f"Item: {key}, Quantity: {value[0]}, Price: ${value[1]}")

# Step 2: Add, Remove, and Update Items

# Add a new item to the inventory (e.g., "mango": (15, 3.0)).
inventory["strawberry"] = (20, 4)
print(f"Adding a new item: {list(inventory.keys())[-1]}")

# Remove an item from the inventory.
del inventory["lychee"]

# Update the quantity or price of an existing item.
inventory["watermelon"] = [5, 3]

# Step 3: Display the Inventory
print("Updated inventory:")
# Write a loop to display all items in the inventory in a friendly format. For example:
for key, value in inventory.items():
    print(f"Item: {key}, Quantity: {value[0]}, Price: ${value[1]}")

# Step 4: Bonus - Calculate Total Value
# Add a feature to calculate and display the total value of the inventory by multiplying the quantity and price of each item.
total_val = 0
for value in inventory.values():
    total_val += value[0] * value[1]
print(f"Total value of inventory: ${total_val}")