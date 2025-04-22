"""Tests for the AI module."""

import pytest
from python_ai_coding_standards.ai import (
    get_standards_markdown,
    get_example,
    suggest_improvements,
    get_project_structure,
    get_pyproject_toml_example,
    generate_standard_response,
)


def test_get_standards_markdown() -> None:
    """Test that get_standards_markdown returns a non-empty markdown string."""
    markdown = get_standards_markdown()
    assert isinstance(markdown, str)
    assert len(markdown) > 0
    assert "# Python Coding Standards for AI Assistants" in markdown


def test_get_example() -> None:
    """Test that get_example returns a valid code example."""
    example = get_example("design_patterns")
    assert isinstance(example, str)
    assert len(example) > 0
    assert "class" in example or "def" in example


def test_get_example_invalid_category() -> None:
    """Test that get_example raises ValueError for an invalid category."""
    with pytest.raises(ValueError):
        get_example("invalid_category")  # type: ignore


def test_suggest_improvements() -> None:
    """Test that suggest_improvements returns suggestions for problematic code."""
    code_snippet = """
def process_data(items=[]):
    results = []
    for item in items:
        try:
            results.append(item * 2)
        except:
            pass
    return results
"""
    suggestions = suggest_improvements(code_snippet)
    assert len(suggestions) > 0
    assert any("type hints" in suggestion.lower() for suggestion in suggestions)
    assert any("mutable default" in suggestion.lower() for suggestion in suggestions)
    assert any("specific exceptions" in suggestion.lower() for suggestion in suggestions)


def test_get_project_structure() -> None:
    """Test that get_project_structure returns a non-empty string."""
    structure = get_project_structure()
    assert isinstance(structure, str)
    assert len(structure) > 0
    assert "project/" in structure
    assert "src/" in structure
    assert "tests/" in structure


def test_get_pyproject_toml_example() -> None:
    """Test that get_pyproject_toml_example returns a valid toml string."""
    toml_content = get_pyproject_toml_example()
    assert isinstance(toml_content, str)
    assert len(toml_content) > 0
    assert "[build-system]" in toml_content
    assert "[tool.ruff]" in toml_content
    assert "[tool.mypy]" in toml_content


def test_generate_standard_response() -> None:
    """Test that generate_standard_response returns appropriate responses."""
    # Test structure query
    structure_response = generate_standard_response("project structure")
    assert "Project Structure" in structure_response
    assert "src-layout" in structure_response.lower()

    # Test toolchain query
    tools_response = generate_standard_response("recommended tools")
    assert "Toolchain" in tools_response
    assert "Ruff" in tools_response
    assert "MyPy" in tools_response

    # Test OOP query
    oop_response = generate_standard_response("OOP principles")
    assert "OOP Best Practices" in oop_response
    assert "Single Responsibility Principle" in oop_response

    # Test default response
    default_response = generate_standard_response("give me some advice")
    assert "Python Coding Standards - Quick Reference" in default_response
