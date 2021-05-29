import sys

import click

from clean_docker.main import main


@click.command(help="Remove Docker images, containers, volumes, and networks")
@click.version_option()
def cli() -> None:
    if click.confirm("Remove all Docker artifacts?"):
        sys.exit(main())
    else:
        click.echo("Abort", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
