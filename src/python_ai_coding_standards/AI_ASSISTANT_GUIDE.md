# Guide for AI Assistants Using Python AI Coding Standards

This guide is specifically designed for AI assistants to help them effectively use this package to apply Python coding standards consistently.

## Quick Start

When working on Python projects, you can access Python coding standards from this package using the following approaches:

### 1. Direct API Access

```python
from python_ai_coding_standards.core.api import for_ai_assistant

# Get a summary of standards for AI use
standards = for_ai_assistant()

# Use these standards to guide code generation
```

### 2. Helper Functions for Common Queries

```python
from python_ai_coding_standards.ai import (
    get_standards_markdown,
    get_example,
    suggest_improvements,
    get_project_structure,
    get_pyproject_toml_example,
    generate_standard_response,
)

# Generate a formatted markdown response for common queries
response = generate_standard_response("project structure")

# Get code examples for specific standards
oop_example = get_example("oop_principles", "Single Responsibility Principle (SRP)")

# Suggest improvements for code
suggestions = suggest_improvements(user_code_snippet)

# Get project structure recommendation
structure = get_project_structure()

# Get a pyproject.toml example
toml_example = get_pyproject_toml_example()
```

## Key Practices to Apply

When generating or reviewing Python code, prioritize these practices:

1. **Always Add Type Hints**: Use PEP 695 generic syntax where appropriate.
   ```python
   def process_items[T](items: list[T]) -> list[T]:
       return [item for item in items if item is not None]
   ```

2. **Use Modern Python Features**:
   - Dataclasses for data containers
   - Pattern matching for complex conditionals
   - Context managers for resource handling
   - Async/await for asynchronous code

3. **Follow SOLID Principles**:
   - Single Responsibility Principle
   - Open/Closed Principle
   - Interface Segregation
   - Dependency Inversion
   - Composition over inheritance

4. **Project Structure**: Recommend src-layout with pyproject.toml

5. **Toolchain**: Suggest Ruff, MyPy, Pytest, and Hatch

## Responding to Specific Queries

### When Asked About Project Setup:

1. Recommend the src-layout structure
2. Suggest using Hatch for project management
3. Provide a pyproject.toml example with proper configuration
4. Mention Ruff for linting and formatting, MyPy for type checking

### When Asked About Code Quality:

1. Recommend comprehensive testing with Pytest
2. Emphasize strict type checking with MyPy
3. Suggest Ruff for linting and enforcing style
4. Explain the importance of documenting public APIs

### When Reviewing Code:

1. Check for type hints and suggest improvements
2. Look for OOP principle violations
3. Identify opportunities to use modern Python features
4. Suggest test coverage improvements

## Example Code Standards

### OOP Principles Example

```python
# Bad: Class doing too much
class UserManager:
    def create_user(self) -> None: ...
    def send_email(self) -> None: ...
    def validate_password(self) -> None: ...

# Good: Separate responsibilities
class UserCreator:
    def create_user(self) -> None: ...

class EmailService:
    def send_email(self) -> None: ...

class PasswordValidator:
    def validate_password(self) -> None: ...
```

### Error Handling Example

```python
# Bad: Generic exception handling
try:
    result = process_data(input_data)
except Exception as e:
    log_error(str(e))

# Good: Specific exception handling
try:
    result = process_data(input_data)
except ValueError as e:
    log_error(f"Invalid data format: {e}")
except ConnectionError as e:
    log_error(f"Network error: {e}")
except Exception as e:  # Still catch unexpected errors as last resort
    log_error(f"Unexpected error: {e}")
    raise  # Re-raise to propagate the error
```