# Week 9: Advanced Python Concepts

## Learning Objectives
By the end of this week, you will be able to:
- Create and use generators and iterators
- Implement context managers
- Understand metaclasses (basic level)
- Write asynchronous code with async/await
- Optimize code performance using advanced techniques

## Daily Breakdown

### Day 1: Generators and Iterators
- Understanding iterators (__iter__, __next__)
- Generator functions with yield
- Generator expressions
- **Practice**: Memory-efficient data processing

### Day 2: Context Managers
- Understanding context managers
- Using with statement
- Creating custom context managers
- **Practice**: Resource management system

### Day 3: Metaclasses (Introduction)
- What are metaclasses
- type() as a metaclass
- Custom metaclasses (basic)
- **Practice**: Automatic property creation

### Day 4: Asynchronous Programming Basics
- Understanding async/await
- asyncio basics
- Coroutines vs functions
- **Practice**: Async web requests

### Day 5: Performance Optimization
- Profiling Python code
- Memory optimization techniques
- Using collections.deque, set for performance
- **Practice**: Performance comparison tests

### Weekend Project: Asynchronous Web Scraper
Build a concurrent web scraper that efficiently processes multiple URLs using async programming.

## Key Concepts

### Generators
```python
# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator expression
squares = (x**2 for x in range(1000000))  # Memory efficient

# Using generators
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Memory efficient processing
def process_data(data_generator):
    for item in data_generator:
        # Process one item at a time
        yield process_item(item)
```

### Custom Iterator
```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Usage
for num in CountDown(3):
    print(num)  # Prints 3, 2, 1
```

### Context Managers
```python
# Function-based context manager
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    resource = acquire_resource()
    try:
        yield resource
    finally:
        print("Releasing resource")
        release_resource(resource)

# Class-based context manager
class DatabaseConnection:
    def __enter__(self):
        self.connection = create_connection()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")
```

### Async Programming
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Running async code
async def main():
    urls = ['http://example.com', 'http://google.com']
    results = await fetch_multiple_urls(urls)
    return results

# Execute
asyncio.run(main())
```

### Simple Metaclass
```python
class AutoPropertyMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Automatically create properties for attributes ending with '_'
        for key, value in list(namespace.items()):
            if key.endswith('_') and not key.startswith('__'):
                prop_name = key[:-1]
                namespace[prop_name] = property(
                    lambda self, k=key: getattr(self, k),
                    lambda self, val, k=key: setattr(self, k, val)
                )
        return super().__new__(mcs, name, bases, namespace)

class Person(metaclass=AutoPropertyMeta):
    def __init__(self, name, age):
        self.name_ = name
        self.age_ = age

# Usage
p = Person("Alice", 30)
print(p.name)  # Accesses name_ through property
p.age = 31     # Sets age_ through property
```

## Performance Optimization

### Profiling
```python
import cProfile
import time

def slow_function():
    time.sleep(0.1)
    return sum(range(1000))

# Profile the function
cProfile.run('slow_function()')

# Line profiler (requires line_profiler package)
@profile
def detailed_function():
    # Each line will be profiled
    data = list(range(1000))
    result = sum(data)
    return result
```

### Memory Optimization
```python
# Use __slots__ to reduce memory usage
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Use generators for large datasets
def process_large_dataset(data):
    # Instead of creating a large list
    return (process_item(item) for item in data)

# Use collections.deque for frequent insertions/deletions
from collections import deque
queue = deque()  # More efficient than list for queue operations
```

## Advanced Patterns

### Coroutine Decorator
```python
def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Prime the coroutine
        return gen
    return wrapper

@coroutine
def moving_average():
    total = 0
    count = 0
    average = 0
    while True:
        value = yield average
        total += value
        count += 1
        average = total / count
```

### Async Context Manager
```python
class AsyncDatabaseConnection:
    async def __aenter__(self):
        self.connection = await create_async_connection()
        return self.connection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

# Usage
async with AsyncDatabaseConnection() as conn:
    await conn.execute("SELECT * FROM users")
```

## When to Use Advanced Concepts

### Generators
- Processing large datasets that don't fit in memory
- Creating infinite sequences
- Pipeline data processing

### Context Managers
- Resource management (files, connections, locks)
- Temporary state changes
- Exception-safe cleanup

### Async Programming
- I/O-bound operations (web requests, file operations)
- Concurrent processing
- Real-time applications

### Metaclasses
- Framework development
- Automatic code generation
- Advanced ORM implementations
- **Note**: "If you're not sure whether you need metaclasses, you don't need them"

## Assessment
- [ ] Can create and use generators effectively
- [ ] Understands iterator protocol
- [ ] Can implement context managers
- [ ] Basic understanding of metaclasses
- [ ] Can write simple async code
- [ ] Knows performance optimization techniques
- [ ] Completed the weekend project

---
**Previous**: [Week 8: Advanced OOP & Functional Programming](../../02-intermediate/week-08-advanced-oop-functional/) | **Next**: [Week 10: Libraries and Package Management](../week-10-libraries-packages/)
