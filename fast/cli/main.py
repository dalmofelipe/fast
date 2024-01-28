from typer import Typer
from rich import print
from typing import Optional
from subprocess import run

from fast.config.environment import Settings

PORT = Settings.PORT

cli = Typer(help='CLI FastApi101')


@cli.command(
    'runserver'
)
def cmd_runserver():
    f"""
    Inicia o WebServer do projeto por na porta ENVIRONMENT {PORT} ou 8000
    """
    run(['uvicorn', 'fast.web.main:webapp', f'--port={PORT}', '--reload'])


@cli.command(
    'hello'
)
def cmd_hello(name: Optional[str | None] = 'World'):
    """
    Hello World
    """
    print(f'Hello {name}!')


@cli.command(
    'ping'
)
def cmd_ping():
    """
    Comando para teste da CLI
    """
    print(f'PONG!')
