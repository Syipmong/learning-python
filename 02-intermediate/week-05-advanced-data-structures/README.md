# Week 5: Advanced Data Structures

## Learning Objectives
By the end of this week, you will be able to:
- Write list comprehensions for efficient list creation
- Create dictionary comprehensions
- Work with nested data structures
- Handle JSON data effectively
- Combine multiple data structures for complex problems

## Daily Breakdown

### Day 1: List Comprehensions
- Basic list comprehension syntax
- Filtering with conditions
- Transforming data
- **Practice**: Data filtering and transformation

### Day 2: Dictionary and Set Comprehensions
- Dictionary comprehension syntax
- Set comprehensions
- When to use comprehensions vs loops
- **Practice**: Data aggregation tasks

### Day 3: Nested Data Structures
- Lists of lists (2D arrays)
- Lists of dictionaries
- Dictionaries of lists
- **Practice**: Student grade management system

### Day 4: Working with JSON
- JSON format basics
- json.loads() and json.dumps()
- Reading/writing JSON files
- **Practice**: Configuration file manager

### Day 5: Complex Data Processing
- Combining data structures
- Data transformation pipelines
- Performance considerations
- **Practice**: Data analysis scenarios

### Weekend Project: Contact Management System
Build a comprehensive contact manager using nested data structures and JSON persistence.

## Key Concepts

### List Comprehensions
```python
# Basic syntax
[expression for item in iterable]

# With condition
[expression for item in iterable if condition]

# Examples
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dictionary Comprehensions
```python
# Basic syntax
{key_expr: value_expr for item in iterable}

# Example
word_lengths = {word: len(word) for word in ['python', 'java', 'c++']}
```

### Nested Structures
```python
# Matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Students database
students = [
    {'name': 'Alice', 'grades': [85, 90, 78]},
    {'name': 'Bob', 'grades': [92, 88, 84]}
]
```

## Performance Tips
- List comprehensions are generally faster than equivalent for loops
- Use generators for large datasets to save memory
- Consider using collections.defaultdict for complex nested structures
- JSON is text-based, so large datasets might be slow

## Common Patterns
```python
# Flattening nested lists
flat = [item for sublist in nested_list for item in sublist]

# Grouping data
from collections import defaultdict
groups = defaultdict(list)
for item in data:
    groups[item.category].append(item)

# JSON handling
import json
data = json.loads(json_string)
json_string = json.dumps(data, indent=2)
```

## Assessment
- [ ] Can write efficient list comprehensions
- [ ] Understands dictionary and set comprehensions
- [ ] Comfortable with nested data structures
- [ ] Can work with JSON data
- [ ] Completed practical data processing tasks
- [ ] Completed the weekend project

---
**Previous**: [Week 4: Data Structures](../week-04-data-structures/) | **Next**: [Week 6: File Handling & Exception Handling](../week-06-file-handling-exceptions/)
