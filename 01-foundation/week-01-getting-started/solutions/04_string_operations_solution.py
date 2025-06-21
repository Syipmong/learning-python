# Solution 4: String Formatting and Operations

# 1. Create variables for first name and last name
first_name = "Alice"
last_name = "Johnson"

# 2. Create a full name by combining first and last name
full_name = f"{first_name} {last_name}"
# Alternative: full_name = first_name + " " + last_name

# 3. Convert the full name to different cases
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()
full_name_title = full_name.title()

# 4. Create a formatted introduction
introduction = f"Hello, my name is {full_name_upper}, but you can call me {first_name.lower()}."

# 5. Count the number of characters in your full name (excluding spaces)
char_count = len(full_name.replace(" ", ""))

# 6. Check if your name contains the letter 'a' (case insensitive)
contains_a = 'a' in full_name.lower()

# 7. Replace all spaces in your full name with underscores
name_with_underscores = full_name.replace(" ", "_")

# 8. Create a username by taking first 3 letters of first name and last 3 of last name
username = first_name[:3].lower() + last_name[-3:].lower()

# Print all results
print("=== String Operations Results ===")
print(f"Full name: {full_name}")
print(f"Uppercase: {full_name_upper}")
print(f"Lowercase: {full_name_lower}")
print(f"Title case: {full_name_title}")
print(f"Introduction: {introduction}")
print(f"Character count (no spaces): {char_count}")
print(f"Contains 'a': {contains_a}")
print(f"With underscores: {name_with_underscores}")
print(f"Username: {username}")

# Additional string methods demonstration
print(f"\nBonus operations:")
print(f"First name starts with 'A': {first_name.startswith('A')}")
print(f"Last name ends with 'son': {last_name.endswith('son')}")
print(f"Full name split into words: {full_name.split()}")
print(f"Reversed full name: {full_name[::-1]}")
