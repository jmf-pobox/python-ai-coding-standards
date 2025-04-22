"""API for accessing Python coding standards.

This module provides functions for AI assistants to query coding standards.
"""

from typing import Any, Literal, TypedDict

from python_ai_coding_standards.standards.data import (
    PROJECT_STRUCTURE,
    DEVELOPMENT_TOOLS,
    OOP_PRINCIPLES,
    DESIGN_PATTERNS,
    DATA_STRUCTURES,
    MODERN_FEATURES,
    FUNCTIONAL_PROGRAMMING,
    ERROR_HANDLING,
    TESTING,
    ENVIRONMENT,
    AI_GUIDELINES,
    PROJECT_TYPES,
)


StandardCategory = Literal[
    "project_structure",
    "development_tools",
    "oop_principles",
    "design_patterns",
    "data_structures",
    "modern_features",
    "functional_programming",
    "error_handling",
    "testing",
    "environment",
    "ai_guidelines",
    "project_types",
]


class StandardInfo(TypedDict):
    """Information about a standard category."""

    title: str
    description: str
    examples: list[dict[str, Any]]
    guidelines: list[str]


_STANDARDS_MAP: dict[StandardCategory, Any] = {
    "project_structure": PROJECT_STRUCTURE,
    "development_tools": DEVELOPMENT_TOOLS,
    "oop_principles": OOP_PRINCIPLES,
    "design_patterns": DESIGN_PATTERNS,
    "data_structures": DATA_STRUCTURES,
    "modern_features": MODERN_FEATURES,
    "functional_programming": FUNCTIONAL_PROGRAMMING,
    "error_handling": ERROR_HANDLING,
    "testing": TESTING,
    "environment": ENVIRONMENT,
    "ai_guidelines": AI_GUIDELINES,
    "project_types": PROJECT_TYPES,
}


def get_all_categories() -> list[tuple[StandardCategory, str]]:
    """Get all available standard categories with their titles.

    Returns:
        A list of tuples containing (category_id, category_title).
    """
    return [(cat, data["title"]) for cat, data in _STANDARDS_MAP.items()]


def get_standard(category: StandardCategory) -> StandardInfo:
    """Get the standards for a specific category.

    Args:
        category: The category of standards to retrieve.

    Returns:
        The standards information for the requested category.

    Raises:
        ValueError: If the category doesn't exist.
    """
    if category not in _STANDARDS_MAP:
        raise ValueError(f"Unknown standard category: {category}")

    return _STANDARDS_MAP[category]


def search_standards(query: str) -> list[tuple[StandardCategory, str, Any]]:
    """Search through all standards for matching content.

    Args:
        query: The search string to look for in standards.

    Returns:
        A list of tuples with (category, matched_field, content) where the query was found.
    """
    results = []
    query = query.lower()

    for category, data in _STANDARDS_MAP.items():
        # Search in title
        if query in data["title"].lower():
            results.append((category, "title", data["title"]))

        # Search in description
        if query in data["description"].lower():
            results.append((category, "description", data["description"]))

        # Search in guidelines
        for guideline in data["guidelines"]:
            if query in guideline.lower():
                results.append((category, "guideline", guideline))

        # Search in examples
        for example in data["examples"]:
            for key, value in example.items():
                if isinstance(value, str) and query in value.lower():
                    results.append((category, f"example.{key}", value))

    return results


def get_project_toolchain() -> dict[str, Any]:
    """Get the recommended toolchain for Python projects.

    Returns:
        A dictionary with tool information.
    """
    return {
        "linter": "ruff",
        "formatter": "ruff format",
        "type_checker": "mypy --strict",
        "test_framework": "pytest",
        "build_system": "hatch",
        "commands": {
            "lint": "hatch run lint",
            "format": "hatch run format",
            "type_check": "hatch run type",
            "test": "hatch run test",
            "dev": "hatch run dev",
        },
    }


def for_ai_assistant() -> dict[str, Any]:
    """Get a summary of standards specifically for AI assistants.

    Returns:
        A dictionary with AI-specific guidance.
    """
    return {
        "general_guidelines": AI_GUIDELINES["guidelines"],
        "project_structure": PROJECT_STRUCTURE["guidelines"],
        "python_version": "3.11+",
        "typing": "Always use type hints, including PEP 695 generics",
        "preferred_tools": {
            "linter": "ruff",
            "type_checker": "mypy --strict",
            "package_manager": "hatch",
        },
        "oop_principles": [str(p["title"]) for p in OOP_PRINCIPLES["examples"]],
        "modern_features": [str(f["title"]) for f in MODERN_FEATURES["examples"]],
    }
