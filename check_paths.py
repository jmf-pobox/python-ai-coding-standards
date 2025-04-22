"""Check import paths."""
import sys
import os

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("\nImport paths:")
for path in sys.path:
    print(f" - {path}")

current_dir = os.path.abspath(os.path.dirname(__file__))
print("\nCurrent directory:", current_dir)
print("Is current directory in sys.path:", current_dir in sys.path)

# Check if src directory exists in the current path
src_dir = os.path.join(current_dir, "src")
print("src directory exists:", os.path.exists(src_dir))

# List contents of src directory
if os.path.exists(src_dir):
    print("\nContents of src directory:")
    for item in os.listdir(src_dir):
        print(f" - {item}")
        
    pkg_dir = os.path.join(src_dir, "python_ai_coding_standards")
    if os.path.exists(pkg_dir):
        print("\nContents of package directory:")
        for item in os.listdir(pkg_dir):
            print(f" - {item}")