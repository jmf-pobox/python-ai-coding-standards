"""Tests for the API module."""
from typing import Any, cast

import pytest

from python_ai_coding_standards.core.api import (
    StandardCategory,
    get_all_categories,
    get_standard,
    search_standards,
    get_project_toolchain,
    for_ai_assistant,
)


def test_get_all_categories() -> None:
    """Test that get_all_categories returns a non-empty list of categories."""
    categories = get_all_categories()
    assert len(categories) > 0
    assert all(isinstance(cat, str) for cat, _ in categories)
    assert all(isinstance(title, str) for _, title in categories)


def test_get_standard() -> None:
    """Test that get_standard returns a standard for a valid category."""
    # Get the first category from the list
    categories = get_all_categories()
    first_category = cast(StandardCategory, categories[0][0])
    
    standard = get_standard(first_category)
    assert isinstance(standard, dict)
    assert "title" in standard
    assert "description" in standard
    assert "guidelines" in standard
    assert "examples" in standard


def test_get_standard_invalid_category() -> None:
    """Test that get_standard raises ValueError for an invalid category."""
    with pytest.raises(ValueError):
        get_standard(cast(StandardCategory, "invalid_category"))


def test_search_standards() -> None:
    """Test that search_standards returns results for a common term."""
    results = search_standards("python")
    assert len(results) > 0
    
    # Check the structure of the first result
    first_result = results[0]
    assert len(first_result) == 3
    assert isinstance(first_result[0], str)  # category
    assert isinstance(first_result[1], str)  # field
    assert isinstance(first_result[2], (str, dict, list))  # content


def test_get_project_toolchain() -> None:
    """Test that get_project_toolchain returns the expected structure."""
    toolchain = get_project_toolchain()
    assert isinstance(toolchain, dict)
    assert "linter" in toolchain
    assert "formatter" in toolchain
    assert "type_checker" in toolchain
    assert "test_framework" in toolchain
    assert "build_system" in toolchain
    assert "commands" in toolchain
    assert isinstance(toolchain["commands"], dict)


def test_for_ai_assistant() -> None:
    """Test that for_ai_assistant returns the expected structure."""
    ai_standards = for_ai_assistant()
    assert isinstance(ai_standards, dict)
    assert "general_guidelines" in ai_standards
    assert "project_structure" in ai_standards
    assert "python_version" in ai_standards
    assert "typing" in ai_standards
    assert "preferred_tools" in ai_standards
    assert "oop_principles" in ai_standards
    assert "modern_features" in ai_standards