# Week 3: Functions and Modules

## Learning Objectives
By the end of this week, you will be able to:
- Define and call functions with parameters
- Use return statements effectively
- Understand variable scope (local vs global)
- Import and use Python modules
- Create your own modules
- Write reusable and organized code

## Daily Breakdown

### Day 1: Function Basics
- Function definition with `def`
- Calling functions
- Parameters vs arguments
- **Practice**: Temperature converter functions

### Day 2: Return Values and Scope
- Return statements
- Functions that return values
- Local vs global variables
- **Practice**: Mathematical operation functions

### Day 3: Advanced Function Features
- Default parameters
- Keyword arguments
- Variable-length arguments (*args, **kwargs)
- **Practice**: Flexible greeting function

### Day 4: Built-in Functions and Modules
- Common built-in functions (len, max, min, sum)
- Importing modules (math, random, datetime)
- Using module functions
- **Practice**: Random number games

### Day 5: Creating Your Own Modules
- Writing your own modules
- Importing from custom modules
- Module organization
- **Practice**: Utility function library

### Weekend Project: Personal Finance Calculator
Create a modular calculator system with separate functions for different financial calculations.

## Key Concepts

### Function Structure
```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional
```

### Scope Rules
- Variables defined inside functions are local
- Global variables can be read but not modified (without `global`)
- Parameters are local to the function

### Module Usage
```python
import math
from random import randint
import my_module as mm
```

## Common Patterns
```python
# Function with default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function with multiple returns
def divide_and_remainder(a, b):
    return a // b, a % b

# Function with variable arguments
def calculate_average(*numbers):
    return sum(numbers) / len(numbers)
```

## Assessment
- [ ] Can write functions with multiple parameters
- [ ] Understands return values and scope
- [ ] Can use built-in functions effectively
- [ ] Successfully imports and uses modules
- [ ] Created custom modules
- [ ] Completed the weekend project

---
**Previous**: [Week 2: Control Structures](../week-02-control-structures/) | **Next**: [Week 4: Data Structures](../../02-intermediate/week-04-data-structures/)
