# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- Run linting: `hatch run lint`
- Run formatter: `hatch run format`
- Run type checking: `hatch run type`
- Run all tests: `hatch run test`
- Run a single test: `hatch run test tests/test_file.py::test_function`
- Run linting and tests: `hatch run all`

## Code Style
- **Line length**: 100 characters max
- **Quotes**: Double quotes for strings
- **Imports**: Sort imports with standard libraries first, then third-party, then local
- **Type hints**: Required on all functions and return values (PEP 695 generics)
- **Error handling**: Use specific exceptions, create custom exception hierarchy
- **Naming**: Use snake_case for variables/functions, PascalCase for classes
- **Project structure**: Follow src-layout with business logic in core/ module
- **Testing**: Write tests for all public methods and functions

## Python Standard
- Python 3.11+ targeting
- Use dataclasses for data containers
- Prefer composition over inheritance
- Use context managers for resource management
- Follow SOLID principles