# Week 4: Data Structures

## Learning Objectives
By the end of this week, you will be able to:
- Create and manipulate lists effectively
- Work with tuples and understand immutability
- Use dictionaries for key-value pair storage
- Implement sets for unique collections
- Choose the appropriate data structure for different scenarios

## Daily Breakdown

### Day 1: Lists - Creation and Basic Operations
- Creating lists
- Accessing elements with indexing
- List slicing
- **Practice**: Student grade manager

### Day 2: Lists - Methods and Manipulation
- append(), insert(), remove(), pop()
- extend(), clear(), count(), index()
- Sorting and reversing lists
- **Practice**: Shopping list manager

### Day 3: Tuples - Immutable Sequences
- Creating tuples
- Tuple unpacking
- When to use tuples vs lists
- **Practice**: Coordinate system

### Day 4: Dictionaries - Key-Value Pairs
- Creating and accessing dictionaries
- Dictionary methods (keys(), values(), items())
- Adding and removing entries
- **Practice**: Contact book

### Day 5: Sets - Unique Collections
- Creating sets
- Set operations (union, intersection, difference)
- When to use sets
- **Practice**: Unique word counter

### Weekend Project: Data Analysis Tool
Create a program that analyzes text data using all data structures learned.

## Key Concepts
- **Mutability**: Lists and dictionaries can be changed, tuples cannot
- **Indexing**: Accessing elements by position
- **Iteration**: Looping through data structures
- **Data Organization**: Choosing the right structure for your data

## Common Operations
```python
# List operations
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 10

# Dictionary operations  
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2
```

## Performance Notes
- Lists: Good for ordered data, frequent appends
- Tuples: Good for fixed data, dictionary keys
- Dictionaries: Fast lookups by key
- Sets: Fast membership testing, unique elements

## Assessment
- [ ] Can create and manipulate all four data structures
- [ ] Understands when to use each data structure
- [ ] Can combine data structures effectively
- [ ] Completed practical exercises
- [ ] Completed the weekend project

---
**Previous**: [Week 3: Functions and Modules](../../01-foundation/week-03-functions-modules/) | **Next**: [Week 5: Advanced Data Structures](../week-05-advanced-data-structures/)
