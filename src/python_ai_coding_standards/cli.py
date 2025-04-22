"""Command-line interface for Python AI Coding Standards.

This module provides a CLI to access coding standards.
"""

import argparse
import json
import sys
from typing import Any, NoReturn, cast

from python_ai_coding_standards.core.api import (
    StandardCategory,
    get_all_categories,
    get_standard,
    search_standards,
    get_project_toolchain,
    for_ai_assistant,
)
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table


console = Console()


def list_categories() -> None:
    """List all available standard categories."""
    table = Table(title="Python Coding Standards Categories")
    table.add_column("Category", style="cyan")
    table.add_column("Description", style="green")

    for category_id, category_title in get_all_categories():
        table.add_row(category_id, category_title)

    console.print(table)


def show_standard(category: StandardCategory) -> None:
    """Display a specific standard category."""
    try:
        standard = get_standard(category)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return

    console.print(Panel(f"[bold cyan]{standard['title']}[/bold cyan]", expand=False))
    console.print(Markdown(standard["description"]))

    # Print guidelines
    console.print("\n[bold green]Guidelines:[/bold green]")
    for i, guideline in enumerate(standard["guidelines"], 1):
        console.print(f"{i}. {guideline}")

    # Print examples
    if standard["examples"]:
        console.print("\n[bold green]Examples:[/bold green]")
        for example in standard["examples"]:
            console.print(f"\n[bold yellow]{example['title']}[/bold yellow]")

            for key, value in example.items():
                if key == "title":
                    continue

                if key in ("code", "good_example", "bad_example"):
                    if value.strip():
                        console.print(Syntax(value.strip(), "python", theme="monokai"))
                elif key == "commands":
                    cmd_table = Table(show_header=True)
                    cmd_table.add_column("Task")
                    cmd_table.add_column("Command")
                    for cmd_name, cmd in value.items():
                        cmd_table.add_row(cmd_name, cmd)
                    console.print(cmd_table)
                else:
                    console.print(f"{key}: {value}")


def search(query: str) -> None:
    """Search across all standards."""
    results = search_standards(query)

    if not results:
        console.print(f"[yellow]No results found for query:[/yellow] {query}")
        return

    console.print(f"[green]Found {len(results)} results for query:[/green] {query}")

    # Group results by category
    by_category: dict[str, list[tuple[str, Any]]] = {}
    for cat, field, content in results:
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append((field, content))

    # Print results by category
    for cat, items in by_category.items():
        cat_std = cat
        std_cat = cat_std if isinstance(cat_std, StandardCategory) else "project_structure"
        std = get_standard(std_cat)
        console.print(f"\n[bold cyan]{std['title']}[/bold cyan]")

        for field, content in items:
            if field == "title":
                console.print(f"[bold yellow]Title:[/bold yellow] {content}")
            elif field == "description":
                console.print(f"[bold yellow]Description:[/bold yellow] {content}")
            elif field.startswith("example."):
                console.print(f"[bold yellow]Example ({field.split('.')[1]}):[/bold yellow]")
                if isinstance(content, str) and content.strip().startswith(("#", "class", "def")):
                    console.print(Syntax(content.strip(), "python", theme="monokai"))
                else:
                    console.print(content)
            else:
                console.print(f"[bold yellow]{field.capitalize()}:[/bold yellow] {content}")


def show_toolchain() -> None:
    """Display the recommended project toolchain."""
    toolchain = get_project_toolchain()

    console.print(
        Panel("[bold cyan]Recommended Python Project Toolchain[/bold cyan]", expand=False)
    )

    tools_table = Table(show_header=True)
    tools_table.add_column("Tool")
    tools_table.add_column("Recommendation")

    tools_table.add_row("Linter", toolchain["linter"])
    tools_table.add_row("Formatter", toolchain["formatter"])
    tools_table.add_row("Type Checker", toolchain["type_checker"])
    tools_table.add_row("Test Framework", toolchain["test_framework"])
    tools_table.add_row("Build System", toolchain["build_system"])

    console.print(tools_table)

    console.print("\n[bold green]Common Commands:[/bold green]")
    for task, command in toolchain["commands"].items():
        console.print(f"[yellow]{task}:[/yellow] {command}")


def for_ai() -> None:
    """Display standards summary specifically for AI assistants."""
    console.print(
        Panel("[bold cyan]Python Coding Standards for AI Assistants[/bold cyan]", expand=False)
    )

    data = for_ai_assistant()

    console.print("\n[bold green]General Guidelines:[/bold green]")
    for i, guideline in enumerate(data["general_guidelines"], 1):
        console.print(f"{i}. {guideline}")

    console.print("\n[bold green]Project Structure:[/bold green]")
    for i, guideline in enumerate(data["project_structure"], 1):
        console.print(f"{i}. {guideline}")

    console.print("\n[bold green]Technical Requirements:[/bold green]")
    console.print(f"[yellow]Python version:[/yellow] {data['python_version']}")
    console.print(f"[yellow]Typing:[/yellow] {data['typing']}")

    console.print("\n[bold green]Preferred Tools:[/bold green]")
    for tool, value in data["preferred_tools"].items():
        console.print(f"[yellow]{tool}:[/yellow] {value}")

    console.print("\n[bold green]OOP Principles:[/bold green]")
    for i, principle in enumerate(data["oop_principles"], 1):
        console.print(f"{i}. {principle}")

    console.print("\n[bold green]Modern Features:[/bold green]")
    for i, feature in enumerate(data["modern_features"], 1):
        console.print(f"{i}. {feature}")


def export_json(output_path: str) -> None:
    """Export all standards as JSON."""
    data = {
        "categories": dict(get_all_categories()),
        "standards": {},
    }

    for cat_id, _ in get_all_categories():
        cat_std = cat_id
        std_cat = cat_std if isinstance(cat_std, StandardCategory) else "project_structure"
        data["standards"][cat_id] = get_standard(std_cat)

    try:
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        console.print(f"[green]Standards exported to:[/green] {output_path}")
    except OSError as e:
        console.print(f"[bold red]Error exporting standards:[/bold red] {e}")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Python AI Coding Standards CLI",
        epilog="Use this tool to access and explore Python coding standards",
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # List categories command
    subparsers.add_parser("list", help="List all standard categories")

    # Show standard command
    show_parser = subparsers.add_parser("show", help="Show a specific standard")
    show_parser.add_argument(
        "category",
        choices=[cat for cat, _ in get_all_categories()],
        help="The standard category to display",
    )

    # Search command
    search_parser = subparsers.add_parser("search", help="Search through standards")
    search_parser.add_argument("query", help="The search query")

    # Toolchain command
    subparsers.add_parser("toolchain", help="Show recommended project toolchain")

    # AI command
    subparsers.add_parser("ai", help="Show standards summary for AI assistants")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export standards as JSON")
    export_parser.add_argument(
        "output",
        help="Output file path (e.g., standards.json)",
    )

    return parser.parse_args()


def main() -> NoReturn:
    """Main entry point for the CLI."""
    args = parse_args()

    if args.command == "list":
        list_categories()
    elif args.command == "show":
        show_standard(cast(StandardCategory, args.category))
    elif args.command == "search":
        search(args.query)
    elif args.command == "toolchain":
        show_toolchain()
    elif args.command == "ai":
        for_ai()
    elif args.command == "export":
        export_json(args.output)
    else:
        list_categories()

    sys.exit(0)


if __name__ == "__main__":
    main()
