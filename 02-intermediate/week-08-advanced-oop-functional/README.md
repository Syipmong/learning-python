# Week 8: Advanced OOP & Functional Programming

## Learning Objectives
By the end of this week, you will be able to:
- Implement polymorphism and encapsulation effectively
- Use magic methods (dunder methods)
- Create and use decorators
- Apply functional programming concepts
- Combine OOP and functional programming paradigms

## Daily Breakdown

### Day 1: Polymorphism and Encapsulation
- Method overriding and polymorphism
- Abstract base classes
- Private and protected attributes
- **Practice**: Shape hierarchy with polymorphic methods

### Day 2: Magic Methods (Dunder Methods)
- Common magic methods (__str__, __repr__, __len__)
- Operator overloading (__add__, __eq__, __lt__)
- Context managers (__enter__, __exit__)
- **Practice**: Custom container class

### Day 3: Decorators Basics
- Understanding decorators
- Function decorators
- Decorator syntax (@decorator)
- **Practice**: Timing and logging decorators

### Day 4: Advanced Decorators and Functional Programming
- Decorators with arguments
- Class decorators
- Lambda functions
- **Practice**: Validation decorators

### Day 5: Functional Programming Concepts
- Higher-order functions (map, filter, reduce)
- Function composition
- Immutability concepts
- **Practice**: Data processing pipeline

### Weekend Project: Advanced Banking System
Build a sophisticated banking system using advanced OOP concepts, decorators, and functional programming techniques.

## Key Concepts

### Magic Methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"Book: {self.title}"
    
    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.title == other.title
    
    def __lt__(self, other):
        return self.pages < other.pages
```

### Decorators
```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with arguments
def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
        return wrapper
    return decorator

@retry(3)
def unreliable_function():
    # Might fail occasionally
    pass
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "Running"
```

### Functional Programming
```python
# Higher-order functions
numbers = [1, 2, 3, 4, 5]

# Map - transform each element
squared = list(map(lambda x: x**2, numbers))

# Filter - select elements
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce - combine elements
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)

# Function composition
def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

composed = compose(multiply_by_two, add_one)
result = composed(5)  # (5 + 1) * 2 = 12
```

## Design Patterns

### Factory Pattern
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
```

### Observer Pattern
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")
```

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## Best Practices

### OOP Best Practices
- Favor composition over inheritance
- Keep classes focused on a single responsibility
- Use abstract base classes for common interfaces
- Implement __str__ and __repr__ for debugging

### Functional Programming Best Practices
- Prefer pure functions (no side effects)
- Use immutable data structures when possible
- Compose simple functions to build complex behavior
- Use list comprehensions over map/filter when clearer

### Decorator Best Practices
- Use functools.wraps to preserve function metadata
- Keep decorators simple and focused
- Document decorator behavior clearly
- Consider using classes for complex decorators

## Assessment
- [ ] Can implement polymorphic behavior effectively
- [ ] Comfortable with magic methods
- [ ] Can create and use decorators
- [ ] Understands functional programming concepts
- [ ] Can combine OOP and functional paradigms
- [ ] Completed the weekend project

---
**Previous**: [Week 7: Object-Oriented Programming](../week-07-oop-basics/) | **Next**: [Week 9: Advanced Python Concepts](../../03-advanced/week-09-advanced-concepts/)
