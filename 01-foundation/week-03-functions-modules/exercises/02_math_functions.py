# Exercise 2: Mathematical Operations Functions
# TODO: Create functions for various mathematical operations

def add(a, b):
    """Add two numbers"""
    # TODO: Return the sum of a and b
    pass

def subtract(a, b):
    """Subtract b from a"""
    # TODO: Return a - b
    pass

def multiply(a, b):
    """Multiply two numbers"""
    # TODO: Return the product of a and b
    pass

def divide(a, b):
    """Divide a by b"""
    # TODO: Return a / b, handle division by zero
    pass

def power(base, exponent):
    """Raise base to the power of exponent"""
    # TODO: Return base ** exponent
    pass

def factorial(n):
    """Calculate factorial of n"""
    # TODO: Return n! (n factorial)
    # Remember: 5! = 5 × 4 × 3 × 2 × 1 = 120
    pass

def is_prime(n):
    """Check if a number is prime"""
    # TODO: Return True if n is prime, False otherwise
    # Prime numbers are only divisible by 1 and themselves
    pass

def gcd(a, b):
    """Find the Greatest Common Divisor of two numbers"""
    # TODO: Use Euclidean algorithm
    pass

def lcm(a, b):
    """Find the Least Common Multiple of two numbers"""
    # TODO: Use the formula: LCM(a,b) = (a * b) / GCD(a,b)
    pass

def fibonacci(n):
    """Generate the nth Fibonacci number"""
    # TODO: Return the nth number in Fibonacci sequence
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    pass

# Test your functions
if __name__ == "__main__":
    # TODO: Test all your functions
    print("Testing mathematical functions...")
    
    # Test basic operations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    
    # Test advanced functions
    print(f"2^8 = {power(2, 8)}")
    print(f"5! = {factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(12, 8) = {lcm(12, 8)}")
    print(f"8th Fibonacci number = {fibonacci(8)}")
