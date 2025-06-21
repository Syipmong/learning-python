# Week 7: Object-Oriented Programming (OOP)

## Learning Objectives
By the end of this week, you will be able to:
- Define classes and create objects
- Use attributes and methods effectively
- Implement constructors with __init__
- Apply inheritance to create class hierarchies
- Understand the principles of OOP

## Daily Breakdown

### Day 1: Classes and Objects
- Class definition syntax
- Creating objects (instances)
- Instance attributes
- **Practice**: Person class with basic attributes

### Day 2: Methods and Constructors
- Instance methods
- The `self` parameter
- Constructor method (__init__)
- **Practice**: Bank account class

### Day 3: Attributes and Properties
- Instance vs class attributes
- Private attributes (name mangling)
- Property decorators (@property)
- **Practice**: Student class with grade validation

### Day 4: Inheritance Basics
- Creating child classes
- Method overriding
- super() function
- **Practice**: Animal hierarchy

### Day 5: Multiple Inheritance and Method Resolution
- Multiple inheritance
- Method Resolution Order (MRO)
- When to use inheritance
- **Practice**: Employee management system

### Weekend Project: Library Management System
Build a comprehensive library system with books, members, and transactions using OOP principles.

## Key Concepts

### Class Definition
```python
class MyClass:
    # Class attribute
    class_variable = "shared by all instances"
    
    def __init__(self, instance_var):
        # Instance attribute
        self.instance_var = instance_var
    
    def instance_method(self):
        return f"Instance variable: {self.instance_var}"
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

### Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

## OOP Principles

### 1. Encapsulation
- Bundling data and methods that work on that data
- Controlling access to object internals
- Using private attributes and public interfaces

### 2. Inheritance
- Creating new classes based on existing ones
- Code reuse and establishing relationships
- "is-a" relationships

### 3. Polymorphism
- Objects of different classes responding to the same interface
- Method overriding
- Duck typing in Python

### 4. Abstraction
- Hiding complex implementation details
- Providing simple interfaces
- Abstract base classes

## Common Patterns
```python
# Factory pattern
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)

# Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()
```

## When to Use OOP
- **Use OOP when:**
  - You have data that belongs together with operations
  - You need to model real-world entities
  - You want to reuse code through inheritance
  - You need to maintain state across method calls

- **Don't force OOP when:**
  - Simple functions would be clearer
  - You're just grouping unrelated functions
  - The problem is primarily algorithmic

## Assessment
- [ ] Can define classes with attributes and methods
- [ ] Understands the role of __init__ and self
- [ ] Can implement inheritance hierarchies
- [ ] Uses properties for data validation
- [ ] Applies OOP principles appropriately
- [ ] Completed the weekend project

---
**Previous**: [Week 6: File Handling & Exception Handling](../week-06-file-handling-exceptions/) | **Next**: [Week 8: Advanced OOP & Functional Programming](../week-08-advanced-oop-functional/)
