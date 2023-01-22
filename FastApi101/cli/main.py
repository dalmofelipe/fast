from typer import Typer
from rich import print
from typing import Optional


cli = Typer(help="CLI FastApi101")


@cli.command('hello')
def cmd_hello(
    name: Optional[str|None] = "World"
):
    """
    Hello World
    """
    print(f"Hello {name}!")


@cli.command('ping')
def cmd_ping():
    """
    Comando para reste da CLI
    """
    print(f"PONG!")
