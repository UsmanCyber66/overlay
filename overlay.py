import typer
import subprocess

#!/usr/bin/env python3

app = typer.Typer()

@app.group()
def create():
    """Create resources"""
    pass
    create_app = typer.Typer()

    @create_app.command()
    def network():
        """Create a network"""
        pass

    @create_app.command()
    def node():
        """Create a node"""
        pass

    app.add_typer(create_app, name="create")
@create.command()
def create_network():
    """Create a network"""
    pass

@create.command()
def create_node():
    """Create a node"""
    pass

if __name__ == "__main__":
    app()