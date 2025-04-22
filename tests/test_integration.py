"""Integration tests for the python-ai-coding-standards package."""

import importlib.util
import sys
from collections.abc import Generator
from typing import Any

import pytest


@pytest.fixture
def standard_modules() -> Generator[dict[str, Any], None, None]:
    """Fixture to import all necessary modules."""
    modules = {}

    # Import the main module
    import python_ai_coding_standards

    modules["main"] = python_ai_coding_standards

    # Import the core API module
    from python_ai_coding_standards.core import api

    modules["api"] = api

    # Import the AI module
    from python_ai_coding_standards import ai

    modules["ai"] = ai

    # Import the standards data module
    from python_ai_coding_standards.standards import data

    modules["data"] = data

    yield modules


def test_package_import(standard_modules: dict[str, Any]) -> None:
    """Test that all package modules can be imported successfully."""
    assert "__version__" in dir(standard_modules["main"])
    assert "get_standard" in dir(standard_modules["api"])
    assert "get_standards_markdown" in dir(standard_modules["ai"])
    assert "PROJECT_STRUCTURE" in dir(standard_modules["data"])


def test_integration_api_to_ai(standard_modules: dict[str, Any]) -> None:
    """Test the integration between the API and AI modules."""
    api_module = standard_modules["api"]
    ai_module = standard_modules["ai"]

    # Test that AI module can access standards via API
    all_categories = api_module.get_all_categories()
    assert len(all_categories) > 0

    first_category = all_categories[0][0]
    example = ai_module.get_example(first_category)
    assert isinstance(example, str)
    assert len(example) > 0


def test_cli_module_importable() -> None:
    """Test that the CLI module can be imported."""
    # Check if the CLI module exists
    cli_spec = importlib.util.find_spec("python_ai_coding_standards.cli")
    assert cli_spec is not None

    # Try to import it
    cli_module = importlib.util.module_from_spec(cli_spec)
    sys.modules["python_ai_coding_standards.cli"] = cli_module
    cli_spec.loader.exec_module(cli_module)  # type: ignore

    # Check that the main function exists
    assert hasattr(cli_module, "main")


def test_ai_standards_response_generation(standard_modules: dict[str, Any]) -> None:
    """Test that the AI module can generate standard responses."""
    ai_module = standard_modules["ai"]

    # Test various query types
    responses = [
        ai_module.generate_standard_response("project structure"),
        ai_module.generate_standard_response("recommended tools"),
        ai_module.generate_standard_response("OOP principles"),
        ai_module.generate_standard_response("modern Python features"),
        ai_module.generate_standard_response("testing"),
        ai_module.generate_standard_response("functional programming"),
        ai_module.generate_standard_response("error handling"),
    ]

    # Verify that all responses are non-empty strings with markdown formatting
    for response in responses:
        assert isinstance(response, str)
        assert len(response) > 0
        assert "##" in response  # Markdown heading
