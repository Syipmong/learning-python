# Week 6: File Handling & Exception Handling

## Learning Objectives
By the end of this week, you will be able to:
- Read from and write to text files
- Work with CSV files using the csv module
- Handle exceptions gracefully with try/except blocks
- Create custom exceptions
- Build robust programs that handle errors

## Daily Breakdown

### Day 1: Basic File Operations
- Opening and closing files
- Reading file contents (read(), readline(), readlines())
- Writing to files
- **Practice**: Text file processor

### Day 2: File Context Managers
- Using `with` statement for file handling
- Automatic file closing
- File modes (r, w, a, r+, etc.)
- **Practice**: Log file analyzer

### Day 3: CSV File Handling
- Reading CSV files with csv.reader
- Writing CSV files with csv.writer
- Working with DictReader and DictWriter
- **Practice**: Student data processor

### Day 4: Exception Handling
- Understanding common exceptions
- try/except/else/finally blocks
- Handling specific exceptions
- **Practice**: Robust file operations

### Day 5: Custom Exceptions
- Creating custom exception classes
- When to use custom exceptions
- Exception best practices
- **Practice**: Input validation system

### Weekend Project: Personal Expense Tracker
Build a file-based expense tracking system with CSV storage and comprehensive error handling.

## Key Concepts

### File Operations
```python
# Basic file reading
with open('filename.txt', 'r') as file:
    content = file.read()

# Writing to file
with open('filename.txt', 'w') as file:
    file.write('Hello, World!')
```

### CSV Handling
```python
import csv

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
```

### Exception Handling
```python
try:
    # Code that might raise an exception
    result = 10 / user_input
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print(f"Result: {result}")
finally:
    print("This always runs")
```

### Custom Exceptions
```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

raise CustomError("Something went wrong!")
```

## File Modes
- `'r'`: Read (default)
- `'w'`: Write (overwrites existing file)
- `'a'`: Append
- `'r+'`: Read and write
- `'b'`: Binary mode (e.g., 'rb', 'wb')

## Exception Hierarchy
```
BaseException
 +-- SystemExit
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- KeyError
      |    +-- IndexError
      +-- ValueError
      +-- TypeError
```

## Best Practices
- Always use context managers (`with` statement) for file operations
- Handle specific exceptions rather than using bare `except:`
- Use finally blocks for cleanup code
- Create meaningful error messages
- Log errors for debugging

## Assessment
- [ ] Can read and write files safely
- [ ] Comfortable with CSV file operations
- [ ] Understands exception handling patterns
- [ ] Can create and use custom exceptions
- [ ] Builds robust, error-resistant programs
- [ ] Completed the weekend project

---
**Previous**: [Week 5: Advanced Data Structures](../week-05-advanced-data-structures/) | **Next**: [Week 7: Object-Oriented Programming](../week-07-oop-basics/)
