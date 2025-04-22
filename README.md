# Python AI Coding Standards

A package that provides Python coding standards for AI assistants to reference.

## Installation

```bash
pip install python-ai-coding-standards
```

## Usage

### Command Line Interface

Access coding standards through the CLI:

```bash
# List all standard categories
pystandards list

# Show a specific standard category
pystandards show oop_principles

# Search across all standards
pystandards search "dataclass"

# Show recommended toolchain
pystandards toolchain

# Get summary for AI assistants
pystandards ai

# Export all standards as JSON
pystandards export standards.json
```

### Using in Code

```python
from python_ai_coding_standards.core.api import (
    get_all_categories,
    get_standard,
    search_standards,
    for_ai_assistant,
)

# Get all standard categories
categories = get_all_categories()

# Get a specific standard
oop_principles = get_standard("oop_principles")

# Search across all standards
results = search_standards("dataclass")

# Get standards summary for AI assistants
ai_standards = for_ai_assistant()
```

### For AI Assistants

If you're an AI assistant, you can access the structured coding standards to help generate Python code that follows best practices:

1. Install the package in the project
2. Import standards from `python_ai_coding_standards.core.api`
3. Use the `for_ai_assistant()` function to get a summary of standards
4. Reference specific standards when generating or reviewing code

## Standards Categories

The following standard categories are available:

- Project Structure
- Development Tools
- OOP Principles
- Design Patterns
- Pythonic Data Structures
- Modern Python Features
- Functional Programming
- Error Handling
- Testing and Quality
- Development Environment
- AI Assistance Guidelines
- Common Project Types

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/python-ai-coding-standards.git
cd python-ai-coding-standards

# Install development dependencies
pip install hatch
hatch shell

# Run tests
hatch run test

# Run linting and type checking
hatch run all
```

## License

MIT License