# Project: Password Strength Checker
# Mandy Lubinski

# Step 1: Input the Password
password = input("Enter a password: ")

# Step 2: Evaluate the Password
errors = []

# Length check
if len(password) < 8:
    errors.append("at least 8 characters")

# Uppercase check
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break
if not has_upper:
    errors.append("one uppercase letter")

# Lowercase check
has_lower = False
for char in password:
    if char.islower():
        has_lower = True
        break
if not has_lower:
    errors.append("one lowercase letter")

# Digit check
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break
if not has_digit:
    errors.append("one digit")

# Special character check
special_characters = "@#$"
has_special = False
for char in password:
    if char in special_characters:
        has_special = True
        break
if not has_special:
    errors.append("one special character")

# Step 3: Output result
if not errors:
    print("Your password is strong! 💪")
else:
    print("Your password needs " + " and ".join(errors) + ".")