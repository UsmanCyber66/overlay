#!/usrbin/env python3

import typer
import overlayfuncs
app = typer.Typer()

create = typer.Typer()

app.add_typer(create, name="create")


@create.command()
def create_network(name: str):
    overlayfuncs.create_network(name)

if __name__ == "__main__":
    app()
