# Solution 3: User Input and Basic Calculator

print("=== Simple Calculator ===")

# Get input from user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform calculations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number if second_number != 0 else "Cannot divide by zero"

# Display results
print(f"\nResults:")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")

# Bonus: More user-friendly formatting
print(f"\nSummary for {first_number} and {second_number}:")
print(f"Sum: {addition:.2f}")
print(f"Difference: {subtraction:.2f}")
print(f"Product: {multiplication:.2f}")
if isinstance(division, float):
    print(f"Quotient: {division:.2f}")
else:
    print(f"Quotient: {division}")
