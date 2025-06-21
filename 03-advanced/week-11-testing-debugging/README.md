# Week 11: Testing and Debugging

## Learning Objectives
By the end of this week, you will be able to:
- Write comprehensive unit tests with unittest and pytest
- Debug Python applications effectively
- Profile code for performance optimization
- Implement test-driven development (TDD)
- Use advanced debugging tools and techniques

## Daily Breakdown

### Day 1: Unit Testing with unittest
- unittest framework basics
- Test cases, test suites, and assertions
- setUp and tearDown methods
- **Practice**: Testing a calculator class

### Day 2: Advanced Testing with pytest
- pytest installation and basic usage
- Fixtures and parameterized tests
- Test coverage measurement
- **Practice**: Comprehensive API testing

### Day 3: Debugging Techniques
- Python debugger (pdb) usage
- IDE debugging features
- Print debugging strategies
- **Practice**: Debug complex algorithms

### Day 4: Test-Driven Development (TDD)
- TDD cycle: Red-Green-Refactor
- Writing tests before implementation
- Benefits and challenges of TDD
- **Practice**: TDD shopping cart implementation

### Day 5: Performance Profiling and Optimization
- Code profiling with cProfile
- Memory profiling techniques
- Performance optimization strategies
- **Practice**: Optimize data processing code

### Weekend Project: Tested Library Development
Create a comprehensive utility library with full test coverage, documentation, and performance benchmarks.

## Key Concepts

### unittest Framework
```python
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Called before each test method"""
        self.calc = Calculator()
    
    def tearDown(self):
        """Called after each test method"""
        pass
    
    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_multiple_operations(self):
        # Test multiple assertions
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertTrue(self.calc.multiply(3, 4) > 10)

if __name__ == '__main__':
    unittest.main()
```

### pytest Framework
```python
import pytest
from calculator import Calculator

# Fixture for common setup
@pytest.fixture
def calculator():
    return Calculator()

# Basic test
def test_addition(calculator):
    assert calculator.add(2, 3) == 5

# Parameterized test
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_addition_multiple_inputs(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

# Test exceptions
def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)

# Skip tests conditionally
@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8 or higher")
def test_new_feature(calculator):
    assert calculator.new_method() is not None

# Mark slow tests
@pytest.mark.slow
def test_performance_intensive():
    # This test takes a long time
    pass

# Run with: pytest -m "not slow" to skip slow tests
```

### Advanced pytest Features
```python
# conftest.py - shared fixtures
import pytest
import tempfile
import os

@pytest.fixture(scope="session")
def database():
    """Session-wide database fixture"""
    db = create_test_database()
    yield db
    db.cleanup()

@pytest.fixture
def temp_file():
    """Create temporary file for testing"""
    with tempfile.NamedTemporaryFile(delete=False) as f:
        yield f.name
    os.unlink(f.name)

# Mock objects
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'success'}
        result = my_api_function()
        assert result['status'] == 'success'
        mock_get.assert_called_once()
```

## Debugging Techniques

### Python Debugger (pdb)
```python
import pdb

def complex_function(data):
    result = []
    for item in data:
        # Set breakpoint
        pdb.set_trace()
        processed = process_item(item)
        result.append(processed)
    return result

# Interactive debugging commands:
# n (next line)
# s (step into function)
# c (continue)
# l (list current code)
# p variable_name (print variable)
# pp variable_name (pretty print)
# q (quit)
```

### Advanced Debugging
```python
# Conditional breakpoints
import pdb

def process_list(items):
    for i, item in enumerate(items):
        if i == 50:  # Debug only when we reach item 50
            pdb.set_trace()
        result = process_item(item)

# Context manager for debugging
from contextlib import contextmanager

@contextmanager
def debug_context(condition=True):
    if condition:
        import pdb; pdb.set_trace()
    try:
        yield
    finally:
        if condition:
            print("Exiting debug context")

# Usage
with debug_context(some_error_condition):
    risky_operation()
```

### Logging for Debugging
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='debug.log'
)

logger = logging.getLogger(__name__)

def complex_calculation(data):
    logger.debug(f"Starting calculation with {len(data)} items")
    
    for i, item in enumerate(data):
        logger.debug(f"Processing item {i}: {item}")
        
        try:
            result = process_item(item)
            logger.info(f"Processed item {i} successfully")
        except Exception as e:
            logger.error(f"Failed to process item {i}: {e}")
            raise
    
    logger.debug("Calculation completed")
    return results
```

## Test-Driven Development (TDD)

### TDD Cycle
```python
# 1. RED: Write a failing test
def test_user_can_register():
    user_service = UserService()
    result = user_service.register("test@example.com", "password123")
    assert result.success is True
    assert result.user.email == "test@example.com"

# 2. GREEN: Write minimal code to pass
class UserService:
    def register(self, email, password):
        # Minimal implementation
        user = User(email=email)
        return RegistrationResult(success=True, user=user)

# 3. REFACTOR: Improve the code
class UserService:
    def __init__(self, user_repository, email_validator):
        self.user_repository = user_repository
        self.email_validator = email_validator
    
    def register(self, email, password):
        if not self.email_validator.is_valid(email):
            return RegistrationResult(success=False, error="Invalid email")
        
        if self.user_repository.find_by_email(email):
            return RegistrationResult(success=False, error="User already exists")
        
        user = User(email=email, password_hash=hash_password(password))
        self.user_repository.save(user)
        return RegistrationResult(success=True, user=user)
```

## Performance Profiling

### cProfile Usage
```python
import cProfile
import pstats

def slow_function():
    # Some slow code
    total = 0
    for i in range(1000000):
        total += i * i
    return total

# Profile the function
cProfile.run('slow_function()', 'profile_stats')

# Analyze results
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 slowest functions
```

### Line Profiler
```python
# Install: pip install line_profiler
# Usage: kernprof -l -v script.py

@profile
def function_to_profile():
    # Line-by-line profiling
    data = list(range(1000))
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2)
    return result
```

### Memory Profiling
```python
# Install: pip install memory_profiler
import tracemalloc

def memory_intensive_function():
    # Start tracing
    tracemalloc.start()
    
    # Your code here
    big_list = [i for i in range(1000000)]
    
    # Get current memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
    
    tracemalloc.stop()
```

## Testing Best Practices

### Test Organization
```python
# tests/test_user_service.py
class TestUserService:
    def setup_method(self):
        """Setup for each test method"""
        self.user_service = UserService()
    
    def test_successful_registration(self):
        # Arrange
        email = "test@example.com"
        password = "secure_password"
        
        # Act
        result = self.user_service.register(email, password)
        
        # Assert
        assert result.success is True
        assert result.user.email == email
    
    def test_duplicate_email_registration(self):
        # Test edge cases
        pass
    
    def test_invalid_email_format(self):
        # Test validation
        pass
```

### Mocking External Dependencies
```python
from unittest.mock import Mock, patch

class TestEmailService:
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        # Arrange
        mock_server = Mock()
        mock_smtp.return_value = mock_server
        email_service = EmailService()
        
        # Act
        result = email_service.send_email("test@example.com", "Subject", "Body")
        
        # Assert
        assert result is True
        mock_server.sendmail.assert_called_once()
```

### Test Coverage
```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run -m pytest

# Generate report
coverage report -m

# Generate HTML report
coverage html
```

## Integration Testing
```python
import pytest
import requests
from your_app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_api_endpoint(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert 'users' in data

def test_user_registration_flow(client):
    # Test complete user registration process
    user_data = {
        'email': 'test@example.com',
        'password': 'secure_password'
    }
    
    response = client.post('/api/register', json=user_data)
    assert response.status_code == 201
    
    # Verify user was created
    response = client.get('/api/users/test@example.com')
    assert response.status_code == 200
```

## Assessment
- [ ] Can write comprehensive unit tests
- [ ] Comfortable with pytest framework
- [ ] Can debug complex issues effectively
- [ ] Understands TDD principles
- [ ] Can profile and optimize code performance
- [ ] Achieved good test coverage
- [ ] Completed the weekend project

---
**Previous**: [Week 10: Libraries and Package Management](../week-10-libraries-packages/) | **Next**: [Week 12: Database Integration](../week-12-database-integration/)
