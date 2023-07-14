from typer import Typer
from rich import print
from typing import Optional
from subprocess import run


cli = Typer(help='CLI FastApi101')


@cli.command('runserver')
def cmd_runserver(port: Optional[int | None] = 8000):
    """
    Inicia o WebServer do projeto por padrão na porta 8000
    """
    run(['uvicorn', 'fast.presentation.web.main:webapp', f'--port={port}', '--reload'])


@cli.command('hello')
def cmd_hello(name: Optional[str | None] = 'World'):
    """
    Hello World
    """
    print(f'Hello {name}!')


@cli.command('ping')
def cmd_ping():
    """
    Comando para teste da CLI
    """
    print(f'PONG!')
