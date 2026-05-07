"""library0 CLI."""
import click


@click.group()
@click.version_option()
def main() -> None:
    """library0 — open-cataloging-protocol tooling."""


@main.command()
def hello() -> None:
    """Smoke-test command."""
    click.echo("library0 is alive")


if __name__ == "__main__":
    main()
