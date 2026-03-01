import typer
import subprocess

#!/usr/bin/env python3

app = typer.Typer()

@app.command()
def hello():
    print("hello")

if __name__ == "__main__":
    app()