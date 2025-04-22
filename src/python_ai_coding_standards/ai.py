"""Module specifically designed for AI assistants to easily access coding standards.

This module provides simplified functions and formatted responses that AI assistants
can use directly in their responses.
"""

from python_ai_coding_standards.core.api import (
    StandardCategory,
    get_standard,
    search_standards,
    for_ai_assistant,
)


def get_standards_markdown() -> str:
    """Get a markdown representation of all standards for AI consumption.

    Returns:
        A markdown-formatted string with the complete standards guide.
    """
    ai_standards = for_ai_assistant()

    markdown = [
        "# Python Coding Standards for AI Assistants\n",
        "## General Guidelines\n",
    ]

    for i, guideline in enumerate(ai_standards["general_guidelines"], 1):
        markdown.append(f"{i}. {guideline}\n")

    markdown.append("\n## Project Structure\n")
    for i, guideline in enumerate(ai_standards["project_structure"], 1):
        markdown.append(f"{i}. {guideline}\n")

    markdown.append("\n## Technical Requirements\n")
    markdown.append(f"- **Python version:** {ai_standards['python_version']}\n")
    markdown.append(f"- **Typing:** {ai_standards['typing']}\n")

    markdown.append("\n## Preferred Tools\n")
    for tool, value in ai_standards["preferred_tools"].items():
        markdown.append(f"- **{tool.capitalize()}:** {value}\n")

    markdown.append("\n## OOP Principles\n")
    for i, principle in enumerate(ai_standards["oop_principles"], 1):
        markdown.append(f"{i}. {principle}\n")

    markdown.append("\n## Modern Features\n")
    for i, feature in enumerate(ai_standards["modern_features"], 1):
        markdown.append(f"{i}. {feature}\n")

    return "".join(markdown)


def get_example(category: StandardCategory, example_title: str | None = None) -> str:
    """Get a code example for a specific standard category.

    Args:
        category: The standard category to get an example for.
        example_title: Optional title of the specific example to retrieve.
            If not provided, returns the first example.

    Returns:
        A string containing the Python code example.

    Raises:
        ValueError: If the category doesn't exist or has no examples.
    """
    standard = get_standard(category)

    if not standard["examples"]:
        raise ValueError(f"No examples available for category: {category}")

    if example_title:
        for example in standard["examples"]:
            if example["title"] == example_title:
                if "code" in example:
                    return str(example["code"]).strip()
                elif "good_example" in example:
                    return str(example["good_example"]).strip()
                else:
                    return str(example)
        raise ValueError(f"Example '{example_title}' not found in category: {category}")
    else:
        example = standard["examples"][0]
        if "code" in example:
            return str(example["code"]).strip()
        elif "good_example" in example:
            return str(example["good_example"]).strip()
        else:
            return str(example)


def suggest_improvements(code_snippet: str) -> list[str]:
    """Analyze a code snippet and suggest improvements based on standards.

    This function uses pattern matching to identify common issues and
    suggest improvements based on the coding standards.

    Args:
        code_snippet: The Python code snippet to analyze.

    Returns:
        A list of improvement suggestions.
    """
    suggestions = []

    # Look for missing type hints
    if "def " in code_snippet and ") ->" not in code_snippet:
        suggestions.append("Add type hints to function return values and parameters")

    # Look for lambda functions with complex logic
    if "lambda" in code_snippet and "if" in code_snippet and "else" in code_snippet:
        suggestions.append(
            "Replace complex lambda functions with named functions for better readability"
        )

    # Look for potential data class candidates
    lines_with_init_assignments = 0
    if "def __init__" in code_snippet:
        for line in code_snippet.split("\n"):
            if "self." in line and " = " in line:
                lines_with_init_assignments += 1

        if lines_with_init_assignments >= 3:
            suggestions.append("Consider using @dataclass to simplify this class definition")

    # Look for using mutable default arguments
    if "def " in code_snippet and "[]" in code_snippet and " = []" in code_snippet:
        suggestions.append("Avoid using mutable default arguments (lists, dicts, etc.)")

    # Look for lack of context managers for file handling
    if "open(" in code_snippet and "with open" not in code_snippet:
        suggestions.append("Use context managers (with statement) for file operations")

    # Look for generic exceptions
    if "except:" in code_snippet or "except Exception:" in code_snippet:
        suggestions.append("Use specific exceptions instead of catching all exceptions")

    # Add recommendation from our standards
    standards_results = search_standards("best practice")
    if standards_results:
        for _, _, content in standards_results[:2]:  # Add up to 2 relevant standards
            if isinstance(content, str) and len(content) < 200:  # Only include short tips
                suggestions.append(content)

    return suggestions


def get_project_structure() -> str:
    """Get the recommended project structure as a formatted string.

    Returns:
        A string containing the project structure.
    """
    standard = get_standard("project_structure")
    for example in standard["examples"]:
        if "title" in example and example["title"] == "Standard project layout":
            return str(example["code"]).strip()

    # Fallback if not found
    return """
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── pyproject.toml
├── README.md
└── .gitignore
""".strip()


def get_pyproject_toml_example() -> str:
    """Get a sample pyproject.toml configuration using recommended tools.

    Returns:
        A string containing the pyproject.toml content.
    """
    return """
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "your-project-name"
version = "0.1.0"
description = "Your project description"
readme = "README.md"
requires-python = ">=3.11"
license = { file = "LICENSE" }
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]

dependencies = [
    # Add your dependencies here
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.0.256",
    "mypy>=1.0.0",
]

[tool.hatch.build.targets.wheel]
packages = ["src/your_package_name"]

[tool.hatch.envs.default]
dependencies = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.0.256",
    "mypy>=1.0.0",
]

[tool.hatch.envs.default.scripts]
test = "pytest {args:tests}"
test-cov = "pytest --cov=your_package_name {args:tests}"
lint = "ruff check src tests"
format = "ruff format src tests"
type = "mypy --strict src"
all = ["lint", "type", "test"]

[tool.ruff]
line-length = 100
target-version = "py311"
select = ["E", "F", "B", "I", "N", "UP", "ANN", "ERA", "RUF"]
ignore = ["ANN101"]  # Missing type annotation for `self`

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "auto"

[tool.mypy]
python_version = "3.11"
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_return_any = true
warn_unreachable = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
strict_optional = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
""".strip()


def generate_standard_response(query: str) -> str:
    """Generate a standard response based on the user query.

    This function is designed to be called by AI assistants to provide
    standardized responses to common queries about Python coding standards.

    Args:
        query: The user query or keyword to respond to.

    Returns:
        A markdown-formatted string response.
    """
    query_lower = query.lower()

    # Project structure query
    if any(term in query_lower for term in ["structure", "layout", "organization"]):
        structure = get_project_structure()
        return f"""
## Recommended Project Structure

```
{structure}
```

**Key points:**
- Use src-layout for better packaging
- Keep tests separate from implementation
- Use pyproject.toml for configuration
- Group related functionality in modules
"""

    # Tools and configuration query
    elif any(term in query_lower for term in ["tools", "toolchain", "configuration", "setup"]):
        return """
## Recommended Toolchain

- **Linter/Formatter:** Ruff
- **Type Checking:** MyPy (--strict)
- **Testing:** Pytest
- **Project Management:** Hatch
- **Python Version:** 3.11+

**Common Commands:**
- `hatch run test`: Run tests
- `hatch run lint`: Run linting
- `hatch run type`: Run type checking
- `hatch run format`: Format code
- `hatch run all`: Run all checks and tests
"""

    # OOP practices query
    elif any(term in query_lower for term in ["oop", "class", "object", "inheritance"]):
        try:
            example = get_example("oop_principles", "Single Responsibility Principle (SRP)")
            return f"""
## OOP Best Practices

1. **Single Responsibility Principle (SRP)**: Each class should have one responsibility
2. **Open/Closed Principle (OCP)**: Open for extension, closed for modification
3. **Interface Segregation**: Prefer focused interfaces over general-purpose ones
4. **Dependency Inversion**: Depend on abstractions, not concretions
5. **Composition over Inheritance**: Prefer composition to inheritance when possible

**Example - Single Responsibility Principle:**
```python
{example}
```
"""
        except ValueError:
            return """
## OOP Best Practices

1. **Single Responsibility Principle (SRP)**: Each class should have one responsibility
2. **Open/Closed Principle (OCP)**: Open for extension, closed for modification
3. **Interface Segregation**: Prefer focused interfaces over general-purpose ones
4. **Dependency Inversion**: Depend on abstractions, not concretions
5. **Composition over Inheritance**: Prefer composition to inheritance when possible
"""

    # Modern Python features query
    elif any(term in query_lower for term in ["modern", "features", "dataclass", "typing"]):
        try:
            example = get_example("modern_features", "Type Annotations and Generics")
            return f"""
## Modern Python Features

1. **Data Classes**: Use for simple data containers
2. **Type Annotations**: Include type hints with PEP 695 generics
3. **Pattern Matching**: Use for complex conditional logic
4. **Async/Await**: For asynchronous programming
5. **Context Managers**: For resource management

**Example - Type Annotations and Generics:**
```python
{example}
```
"""
        except ValueError:
            return """
## Modern Python Features

1. **Data Classes**: Use for simple data containers
2. **Type Annotations**: Include type hints with PEP 695 generics
3. **Pattern Matching**: Use for complex conditional logic
4. **Async/Await**: For asynchronous programming
5. **Context Managers**: For resource management
"""

    # Testing query
    elif any(term in query_lower for term in ["test", "testing", "pytest"]):
        return """
## Testing Best Practices

1. **Unit Tests for All Public Methods**: Ensure all public functionality is tested
2. **Mock External Dependencies**: Use unittest.mock or pytest-mock
3. **Property-Based Testing**: Consider hypothesis for complex logic
4. **Type Checking in CI/CD**: Run mypy as part of CI pipeline
5. **Test Fixtures**: Use pytest fixtures for test setup and reuse

**Example - Basic Unit Test:**
```python
def test_user_creation():
    user = User(name="Test", email="test@example.com")
    assert user.name == "Test"
    assert user.email == "test@example.com"
    assert user.is_active is True  # Default value
```
"""

    # Functional programming query
    elif any(term in query_lower for term in ["functional", "lambda", "comprehension"]):
        try:
            example = get_example("functional_programming", "List Comprehensions")
            return f"""
## Functional Programming in Python

1. **List Comprehensions**: For transforming lists
2. **Generator Expressions**: For memory-efficient sequence processing
3. **Lambda Functions**: For simple operations only
4. **Higher-Order Functions**: Functions that take functions as parameters
5. **Pure Functions**: Functions without side effects

**Example - List Comprehensions:**
```python
{example}
```
"""
        except ValueError:
            return """
## Functional Programming in Python

1. **List Comprehensions**: For transforming lists
2. **Generator Expressions**: For memory-efficient sequence processing
3. **Lambda Functions**: For simple operations only
4. **Higher-Order Functions**: Functions that take functions as parameters
5. **Pure Functions**: Functions without side effects
"""

    # Error handling query
    elif any(term in query_lower for term in ["error", "exception", "handling"]):
        return """
## Error Handling Best Practices

1. **Use Specific Exceptions**: Avoid catching general Exception
2. **Create Custom Exceptions**: For domain-specific errors
3. **Context Managers**: Use for resource management
4. **Document Error Conditions**: In function docstrings
5. **Include Context in Messages**: Make error messages informative

**Example - Custom Exception Hierarchy:**
```python
class DomainError(Exception):
    '''Base exception for all domain errors.'''
    
class UserNotFoundError(DomainError):
    '''Raised when a user cannot be found.'''
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        super().__init__(f"User not found: {user_id}")
```
"""

    # Default response - general guidelines
    else:
        return """
## Python Coding Standards - Quick Reference

1. **Project Structure**: Use src-layout with pyproject.toml
2. **Tools**: Ruff (linting/formatting), MyPy (type checking), Pytest (testing), Hatch (pkg mgmt)
3. **Type Hints**: Always use type annotations with PEP 695 generics
4. **Python Version**: Use Python 3.11+ for new projects
5. **OOP Principles**: Follow SOLID principles, prefer composition over inheritance
6. **Functional Features**: Use list comprehensions, generators, and simple lambdas
7. **Modern Features**: Leverage dataclasses, pattern matching, async/await
8. **Error Handling**: Use specific exceptions and context managers
9. **Testing**: Write unit tests for all public methods

For more details, use the `pystandards` CLI tool or import the `python_ai_coding_standards` package.
"""
