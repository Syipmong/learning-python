# Week 10: Libraries and Package Management

## Learning Objectives
By the end of this week, you will be able to:
- Manage Python packages with pip and virtual environments
- Explore and use popular Python libraries
- Create and distribute your own packages
- Work with APIs and external services
- Understand package versioning and dependency management

## Daily Breakdown

### Day 1: Virtual Environments and Package Management
- Creating virtual environments with venv
- Managing dependencies with pip
- requirements.txt and pip freeze
- **Practice**: Set up project environments

### Day 2: Popular Libraries Overview
- Requests for HTTP operations
- DateTime for date/time handling
- Collections for advanced data structures
- **Practice**: API client development

### Day 3: Creating Your Own Packages
- Package structure and __init__.py
- setup.py and package metadata
- Building and distributing packages
- **Practice**: Utility library creation

### Day 4: Working with APIs
- RESTful API concepts
- Authentication methods
- Error handling for API calls
- **Practice**: Social media API integration

### Day 5: Advanced Package Management
- pip-tools for dependency management
- Poetry as an alternative to pip
- Environment variables and configuration
- **Practice**: Production-ready project setup

### Weekend Project: Multi-Service API Aggregator
Build a service that aggregates data from multiple APIs, packages it as a reusable library, and provides a clean interface.

## Key Concepts

### Virtual Environments
```bash
# Create virtual environment
python -m venv myproject_env

# Activate (Windows)
myproject_env\Scripts\activate

# Activate (Mac/Linux)
source myproject_env/bin/activate

# Install packages
pip install requests pandas flask

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

### Package Structure
```
my_package/
├── setup.py
├── README.md
├── requirements.txt
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── tests/
│       ├── __init__.py
│       ├── test_core.py
│       └── test_utils.py
└── examples/
    └── example_usage.py
```

### setup.py Example
```python
from setuptools import setup, find_packages

setup(
    name="my-awesome-package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-awesome-package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "click>=7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "my-tool=my_package.cli:main",
        ],
    },
)
```

## Popular Libraries

### Requests - HTTP Operations
```python
import requests

# GET request
response = requests.get('https://api.github.com/users/octocat')
data = response.json()

# POST request with data
payload = {'username': 'user', 'password': 'pass'}
response = requests.post('https://api.example.com/login', json=payload)

# Error handling
try:
    response.raise_for_status()  # Raises exception for bad status codes
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### DateTime - Date and Time
```python
from datetime import datetime, timedelta, timezone
import pytz

# Current time
now = datetime.now()
utc_now = datetime.now(timezone.utc)

# Parsing and formatting
date_string = "2023-12-25 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
formatted = parsed_date.strftime("%B %d, %Y at %I:%M %p")

# Timezone handling
eastern = pytz.timezone('US/Eastern')
eastern_time = utc_now.astimezone(eastern)

# Date arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
```

### Collections - Advanced Data Structures
```python
from collections import defaultdict, Counter, deque, namedtuple

# defaultdict - no KeyError
dd = defaultdict(list)
dd['key'].append('value')  # Works even if 'key' doesn't exist

# Counter - counting elements
text = "hello world"
char_count = Counter(text)
print(char_count.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

# deque - efficient queue operations
queue = deque()
queue.appendleft('first')
queue.append('last')
first_item = queue.popleft()

# namedtuple - immutable records
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(f"Point: {p.x}, {p.y}")
```

## API Integration Patterns

### RESTful API Client
```python
import requests
from typing import Dict, List, Optional

class APIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIError(f"API request failed: {e}")
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        return self._request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        return self._request('POST', endpoint, json=data)

class APIError(Exception):
    pass

# Usage
client = APIClient('https://api.example.com', api_key='your-key')
users = client.get('/users', params={'page': 1, 'limit': 10})
```

### Environment Configuration
```python
import os
from typing import Optional

class Config:
    def __init__(self):
        self.api_key = self._get_env_var('API_KEY')
        self.database_url = self._get_env_var('DATABASE_URL')
        self.debug = self._get_env_var('DEBUG', 'False').lower() == 'true'
        self.port = int(self._get_env_var('PORT', '8000'))
    
    def _get_env_var(self, name: str, default: Optional[str] = None) -> str:
        value = os.getenv(name, default)
        if value is None:
            raise ValueError(f"Environment variable {name} is required")
        return value

# Usage with .env file (using python-dotenv)
from dotenv import load_dotenv
load_dotenv()

config = Config()
```

## Package Distribution

### Building and Publishing
```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ my-package
```

### Version Management
```python
# __init__.py
__version__ = "0.1.0"

# Semantic versioning
# MAJOR.MINOR.PATCH
# 1.0.0 - Initial release
# 1.0.1 - Bug fix
# 1.1.0 - New feature (backward compatible)
# 2.0.0 - Breaking changes
```

## Advanced Dependency Management

### pip-tools
```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in
echo "requests>=2.25.0" > requirements.in
echo "click>=7.0" >> requirements.in

# Compile to requirements.txt
pip-compile requirements.in

# Sync environment
pip-sync requirements.txt
```

### Poetry (Alternative)
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Initialize project
poetry init
poetry add requests click
poetry add --group dev pytest black

# Install dependencies
poetry install

# Run in virtual environment
poetry run python script.py
poetry shell
```

## Testing Your Package
```python
# tests/test_core.py
import pytest
from my_package.core import MyClass

def test_my_class_creation():
    obj = MyClass("test")
    assert obj.name == "test"

def test_my_class_method():
    obj = MyClass("test")
    result = obj.process()
    assert result is not None

# Run tests
# pytest tests/
```

## Best Practices

### Package Structure
- Use clear, descriptive names
- Include comprehensive documentation
- Add examples and tutorials
- Implement proper error handling
- Write tests for all functionality

### Dependency Management
- Pin exact versions for applications
- Use ranges for libraries
- Separate development and production dependencies
- Keep dependencies minimal

### API Integration
- Implement proper error handling
- Use connection pooling for multiple requests
- Respect rate limits
- Cache responses when appropriate
- Log API interactions

## Assessment
- [ ] Can create and manage virtual environments
- [ ] Comfortable with popular Python libraries
- [ ] Can create and distribute packages
- [ ] Successfully integrates with APIs
- [ ] Understands dependency management
- [ ] Completed the weekend project

---
**Previous**: [Week 9: Advanced Python Concepts](../week-09-advanced-concepts/) | **Next**: [Week 11: Testing and Debugging](../week-11-testing-debugging/)
