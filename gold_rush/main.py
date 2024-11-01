"""
corrida do ouro - gold *o*
Made from cookiecutter template:
cookiecutter gh:tiagoft/hello_world
"""

import importlib.resources
from rich.console import Console
import typer

import gold_rush


app = typer.Typer(no_args_is_help=True)
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print("Hello! I am corrida do ouro")
    console.print(f"Author: { gold_rush.__author__}")
    console.print(f"Version: { gold_rush.__version__}")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command('demo') # Defines a default action
def run():
    """
    This is a demonstration function that shows how to use the module
    """
    print("Hello world!")
    gold_rush.my_function()
    asset_file = importlib.resources.open_text('gold_rush.assets', 'poetry.txt')
    print(asset_file.read())
    asset_file = importlib.resources.open_text('gold_rush.assets.test_folder', 'test_something.txt')
    print(asset_file.read())

if __name__ == "__main__":
    app()
