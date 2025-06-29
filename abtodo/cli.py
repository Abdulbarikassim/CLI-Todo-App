"""This module provides the AB To-Do CLI.""" # abtodo/cli.py

from typing import Optional

import typer

from abtodo import __app_name__, __version__

app = typer.Typer()


def __version_callback(value: bool)->None: 
    if value: 
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=__version_callback,
        is_eager=True,
    )
) -> None:
    return

