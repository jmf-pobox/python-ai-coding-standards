"""Test script to verify the package can be imported and used."""
import os
import sys

# Add src directory to path
current_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(current_dir, "src")
sys.path.insert(0, src_dir)

print(f"Python version: {sys.version}")
print("Python path:", sys.path[:2])  # Show first two paths
print("Attempting to import modules...")

import python_ai_coding_standards
print(f"Package version: {python_ai_coding_standards.__version__}")

from python_ai_coding_standards.core.api import get_all_categories
categories = get_all_categories()
print(f"Available categories: {len(categories)}")
for cat, title in categories:
    print(f" - {cat}: {title}")

from python_ai_coding_standards.ai import generate_standard_response
response = generate_standard_response("project structure")
print("\nExample response for 'project structure':")
print(response[:200] + "...")  # Show just the first part

print("\nAll imports successful!")