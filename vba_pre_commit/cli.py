"""Console script for vba_pre_commit."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for vba_pre_commit."""
    click.echo("hello")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
