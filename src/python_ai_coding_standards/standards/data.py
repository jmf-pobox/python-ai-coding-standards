"""Python coding standards data.

This module contains structured data for Python coding standards.
"""

PROJECT_STRUCTURE = {
    "title": "Project Structure",
    "description": "Recommended src-layout structure for Python projects",
    "examples": [
        {
            "title": "Standard project layout",
            "code": """
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       ├── api/         # For web/API projects
│       ├── core/        # Core functionality
│       ├── db/          # Database related code
│       ├── models/      # Data models
│       └── schemas/     # Data validation schemas
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── pyproject.toml
├── README.md
└── .gitignore
""",
        }
    ],
    "guidelines": [
        "Use src-layout for all projects",
        "Keep package name and directory structure aligned",
        "Organize related functionality into modules",
        "Use __init__.py files to define public API",
        "Separate tests from implementation code",
        "Use pyproject.toml for project configuration",
    ],
}


DEVELOPMENT_TOOLS = {
    "title": "Development Tools",
    "description": "Recommended tools for Python development",
    "examples": [
        {
            "title": "Common Hatch commands",
            "commands": {
                "tests": "hatch run test",
                "linting": "hatch run lint",
                "type_checking": "hatch run type",
                "formatting": "hatch run format",
                "development_server": "hatch run dev",
            },
        }
    ],
    "guidelines": [
        "Use Ruff for linting and formatting",
        "Use MyPy (with --strict) for static type checking",
        "Use Pytest for testing",
        "Use Hatch for project management",
        "Use Docker for containerization when needed",
        "Always use pyproject.toml for project configuration",
    ],
}


OOP_PRINCIPLES = {
    "title": "Object-Oriented Programming Principles",
    "description": "Best practices for OOP in Python",
    "examples": [
        {
            "title": "Single Responsibility Principle (SRP)",
            "bad_example": """
# Bad: Class doing too much
class UserManager:
    def create_user(self) -> None: ...
    def send_email(self) -> None: ...
    def validate_password(self) -> None: ...
""",
            "good_example": """
# Good: Separate responsibilities
class UserCreator:
    def create_user(self) -> None: ...

class EmailService:
    def send_email(self) -> None: ...

class PasswordValidator:
    def validate_password(self) -> None: ...
""",
        },
        {
            "title": "Open/Closed Principle (OCP)",
            "bad_example": """
# Bad: Modifying existing class
class PaymentProcessor:
    def process_payment(self, payment_type: str) -> None:
        if payment_type == "credit":
            # process credit
        elif payment_type == "paypal":
            # process paypal
""",
            "good_example": """
# Good: Extending through inheritance
class PaymentProcessor:
    def process_payment(self) -> None: ...

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self) -> None: ...

class PayPalProcessor(PaymentProcessor):
    def process_payment(self) -> None: ...
""",
        },
    ],
    "guidelines": [
        "Apply Single Responsibility Principle (SRP)",
        "Follow Open/Closed Principle (OCP)",
        "Use Interface Segregation where appropriate",
        "Apply Dependency Inversion for loosely coupled code",
        "Prefer Composition over Inheritance",
    ],
}


DESIGN_PATTERNS = {
    "title": "Design Patterns",
    "description": "Recommended design patterns for Python",
    "examples": [
        {
            "title": "Factory Pattern",
            "code": """
class PaymentMethodFactory:
    @staticmethod
    def create_payment_method(method_type: str) -> PaymentMethod:
        match method_type:
            case "credit": return CreditCardPayment()
            case "paypal": return PayPalPayment()
            case _: raise ValueError(f"Unknown payment method: {method_type}")
""",
        },
        {
            "title": "Strategy Pattern",
            "code": """
class SortStrategy(Protocol):
    def sort(self, data: list[int]) -> list[int]: ...

class QuickSort:
    def sort(self, data: list[int]) -> list[int]: ...

class MergeSort:
    def sort(self, data: list[int]) -> list[int]: ...
""",
        },
    ],
    "guidelines": [
        "Use Factory Pattern for object creation",
        "Apply Strategy Pattern for interchangeable algorithms",
        "Implement Observer Pattern for event handling",
        "Use Repository Pattern for data access",
        "Use patterns judiciously - don't over-engineer",
    ],
}


DATA_STRUCTURES = {
    "title": "Pythonic Data Structures and Idioms",
    "description": "Recommended data structures and Python idioms",
    "examples": [
        {
            "title": "Appropriate data structures",
            "code": """
# Sets for unique items
unique_items: set[str] = {"apple", "banana", "apple"}

# Dicts for key-value pairs
user_preferences: dict[str, Any] = {
    "theme": "dark",
    "notifications": True
}

# Lists for ordered collections
items: list[str] = ["first", "second", "third"]
""",
        },
        {
            "title": "Built-in types",
            "code": """
# Use Enum for constants
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

# Use NamedTuple for simple data
class Point(NamedTuple):
    x: float
    y: float
""",
        },
    ],
    "guidelines": [
        "Choose appropriate data structures for the use case",
        "Use sets for collections of unique items",
        "Use dictionaries for lookups and mappings",
        "Use lists for ordered collections",
        "Leverage Enum for structured constants",
        "Use NamedTuple and dataclasses for simple data objects",
    ],
}


MODERN_FEATURES = {
    "title": "Modern Python Features",
    "description": "Recent Python features to leverage",
    "examples": [
        {
            "title": "Data Classes",
            "code": """
@dataclass(slots=True)
class User:
    name: str
    email: str
    age: int
    is_active: bool = True
""",
        },
        {
            "title": "Type Annotations and Generics",
            "code": """
def process_items[T](items: list[T]) -> list[T]:
    return [item for item in items if item is not None]
""",
        },
        {
            "title": "Context Managers",
            "code": """
@contextmanager
def managed_resource():
    resource = acquire_resource()
    try:
        yield resource
    finally:
        release_resource(resource)
""",
        },
    ],
    "guidelines": [
        "Use dataclasses for data containers",
        "Apply type annotations with PEP 695 generics",
        "Leverage context managers for resource handling",
        "Use structural pattern matching for complex conditionals",
        "Take advantage of f-strings for string formatting",
    ],
}


FUNCTIONAL_PROGRAMMING = {
    "title": "Functional Programming in Python",
    "description": "Functional programming techniques for Python",
    "examples": [
        {
            "title": "List Comprehensions",
            "code": """
squares = [x**2 for x in range(10) if x % 2 == 0]
""",
        },
        {
            "title": "Generator Expressions",
            "code": """
large_squares = (x**2 for x in range(1000000) if x % 2 == 0)
""",
        },
        {
            "title": "Lambda Functions",
            "good_example": """
# Good: Simple operations
square = lambda x: x**2
""",
            "bad_example": """
# Bad: Complex logic
process_data = lambda x: (x**2 if x > 0 else 0) + (x if x < 10 else 10)
""",
        },
    ],
    "guidelines": [
        "Use list comprehensions over loops when appropriate",
        "Prefer generator expressions for large datasets",
        "Use lambda functions sparingly and only for simple operations",
        "Prefer comprehensions over map/filter/reduce",
        "Use higher-order functions to abstract patterns",
    ],
}


ERROR_HANDLING = {
    "title": "Error Handling and Resource Management",
    "description": "Best practices for handling errors and resources",
    "examples": [
        {
            "title": "Custom exceptions",
            "code": '''
class DomainError(Exception):
    """Base exception for all domain errors."""
    
class UserNotFoundError(DomainError):
    """Raised when a user cannot be found."""
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        super().__init__(f"User not found: {user_id}")
''',
        },
        {
            "title": "Context managers for resources",
            "code": """
with open("file.txt") as f:
    data = f.read()
    
# Or custom context managers
@contextmanager
def database_transaction():
    transaction = db.begin()
    try:
        yield transaction
        transaction.commit()
    except Exception:
        transaction.rollback()
        raise
""",
        },
    ],
    "guidelines": [
        "Use specific exceptions rather than generic ones",
        "Create custom exception hierarchies for domain errors",
        "Always use context managers for resource management",
        "Catch only exceptions you can handle",
        "Include relevant error context in exception messages",
        "Document error conditions in function docstrings",
    ],
}


TESTING = {
    "title": "Testing and Quality",
    "description": "Best practices for testing Python code",
    "examples": [
        {
            "title": "Unit test",
            "code": """
def test_user_creation():
    user = User(name="Test", email="test@example.com")
    assert user.name == "Test"
    assert user.email == "test@example.com"
    assert user.is_active is True  # Default value
""",
        },
        {
            "title": "Mocking dependencies",
            "code": """
@patch("app.services.email_sender.send_email")
def test_welcome_email(mock_send_email):
    service = UserService()
    service.create_user("Test", "test@example.com")
    
    mock_send_email.assert_called_once_with(
        to="test@example.com",
        subject="Welcome to Our Service",
        body=ANY,
    )
""",
        },
    ],
    "guidelines": [
        "Write unit tests for all public methods",
        "Consider property-based testing for complex logic",
        "Always mock external dependencies",
        "Include type checking in CI/CD pipeline",
        "Aim for high test coverage on business logic",
        "Use fixtures to set up test data",
    ],
}


ENVIRONMENT = {
    "title": "Development Environment",
    "description": "Recommended development environment setup",
    "examples": [],
    "guidelines": [
        "Use Python 3.11+ for new projects",
        "Set up Docker for consistent development environments",
        "Use VS Code with Python extensions for a great IDE experience",
        "Manage virtual environments with Hatch or pixi",
        "Configure editor to use Ruff for linting and formatting",
    ],
}


AI_GUIDELINES = {
    "title": "AI Assistance Guidelines",
    "description": "Guidelines for AI assistants generating Python code",
    "examples": [],
    "guidelines": [
        "Always include type hints in generated code",
        "Use modern Python features like PEP 695 generics",
        "Follow the project's linting rules",
        "Maintain or improve test coverage",
        "Consider async/await patterns where appropriate",
        "Follow the src-layout project structure",
        "Use Hatch commands for development tasks",
        "Run ruff check and mypy --strict",
        "Document any non-obvious code decisions",
        "Consider performance implications of suggestions",
    ],
}


PROJECT_TYPES = {
    "title": "Common Project Types",
    "description": "Recommendations for specific types of Python projects",
    "examples": [],
    "guidelines": [
        "Web/API: Use FastAPI, SQLAlchemy, Pydantic, and Alembic",
        "CLI: Use Click or Typer with Rich for terminal output",
        "Data Processing: Use pandas, numpy with proper error handling",
        "Libraries: Design clear public APIs with comprehensive docs",
    ],
}
