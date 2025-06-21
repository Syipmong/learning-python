"""
Week 3 - Exercise 2: Math Functions (Solution)
Advanced mathematical operations with proper validation and error handling.
"""

import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given base and height.
    
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
        
    Returns:
        float: The area of the triangle
        
    Raises:
        ValueError: If base or height is negative
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height


def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial amount
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time (float): Time period in years
        n (int): Number of times interest is compounded per year
        
    Returns:
        tuple: (final_amount, interest_earned)
        
    Raises:
        ValueError: If any parameter is invalid
    """
    if principal < 0:
        raise ValueError("Principal amount cannot be negative")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time period cannot be negative")
    if n <= 0:
        raise ValueError("Compounding frequency must be positive")
    
    final_amount = principal * (1 + rate/n) ** (n * time)
    interest_earned = final_amount - principal
    
    return final_amount, interest_earned


def find_quadratic_roots(a, b, c):
    """
    Find the roots of a quadratic equation ax² + bx + c = 0.
    
    Args:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term
        
    Returns:
        tuple: (root1, root2) or (root,) if single root, or None if no real roots
        
    Raises:
        ValueError: If a is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # One repeated real root
        root = -b / (2*a)
        return (root,)
    else:
        # No real roots
        return None


def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers (list): List of numeric values
        
    Returns:
        dict: Dictionary containing mean, median, mode, and range
        
    Raises:
        ValueError: If the list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Validate all numbers are numeric
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    
    # Calculate mode (most frequent value)
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    mode = modes[0] if len(modes) == 1 else modes  # Return single mode or list
    
    # Calculate range
    range_val = max(numbers) - min(numbers)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': range_val,
        'count': len(numbers)
    }


def main():
    """Main function to demonstrate all mathematical functions."""
    print("=== Math Functions Demonstration ===\n")
    
    # Circle area calculation
    try:
        radius = float(input("Enter circle radius: "))
        area = calculate_circle_area(radius)
        print(f"Circle area: {area:.2f} square units\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Triangle area calculation
    try:
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        area = calculate_triangle_area(base, height)
        print(f"Triangle area: {area:.2f} square units\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Compound interest calculation
    try:
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (as decimal, e.g., 0.05): "))
        time = float(input("Enter time period (years): "))
        n = int(input("Enter compounding frequency per year (default 1): ") or "1")
        
        final_amount, interest = calculate_compound_interest(principal, rate, time, n)
        print(f"Final amount: ${final_amount:.2f}")
        print(f"Interest earned: ${interest:.2f}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Quadratic equation solver
    try:
        print("Solve quadratic equation ax² + bx + c = 0")
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        roots = find_quadratic_roots(a, b, c)
        if roots is None:
            print("No real roots exist\n")
        elif len(roots) == 1:
            print(f"One repeated root: x = {roots[0]:.2f}\n")
        else:
            print(f"Two roots: x₁ = {roots[0]:.2f}, x₂ = {roots[1]:.2f}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Statistics calculation
    try:
        numbers_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in numbers_input.split()]
        
        stats = calculate_statistics(numbers)
        print("Statistics:")
        print(f"  Mean: {stats['mean']:.2f}")
        print(f"  Median: {stats['median']:.2f}")
        print(f"  Mode: {stats['mode']}")
        print(f"  Range: {stats['range']:.2f}")
        print(f"  Count: {stats['count']}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
