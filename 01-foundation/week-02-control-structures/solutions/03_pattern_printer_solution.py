# Solution 3: Pattern Printer

print("=== Pattern Printer ===")

# Pattern 1 - Simple triangle
print("Pattern 1: Simple Triangle")
for i in range(1, 6):
    print("*" * i)

# Pattern 2 - Numbers triangle  
print("\nPattern 2: Numbers Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # New line after each row

# Pattern 3 - Reverse triangle
print("\nPattern 3: Reverse Triangle")
for i in range(5, 0, -1):
    print("*" * i)

# Pattern 4 - Pyramid
print("\nPattern 4: Pyramid")
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Pattern 5 - Multiplication table
print("\nPattern 5: Multiplication Table")
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

print("   " + "-" * 40)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

# Bonus patterns
print("\n" + "="*50)
print("BONUS PATTERNS")
print("="*50)

# Pattern 6 - Diamond
print("\nPattern 6: Diamond")
n = 5
# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Pattern 7 - Number pyramid
print("\nPattern 7: Number Pyramid")
for i in range(1, 6):
    spaces = " " * (5 - i)
    numbers = ""
    for j in range(1, i + 1):
        numbers += str(j)
    for j in range(i - 1, 0, -1):
        numbers += str(j)
    print(spaces + numbers)

# Pattern 8 - Checkerboard
print("\nPattern 8: Checkerboard (8x8)")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("█", end="")
        else:
            print("░", end="")
    print()

# Pattern 9 - Spiral numbers
print("\nPattern 9: Right Triangle with Numbers")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j:2}", end=" ")
    print()

# Pattern 10 - Alphabet triangle
print("\nPattern 10: Alphabet Triangle")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
