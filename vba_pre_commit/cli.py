"""Console script for vba_pre_commit."""
import sys
import click


@click.command()
@click.argument('files', type=str, nargs=-1)
def main(files):
    """Console script for vba_pre_commit."""
    click.echo("hello")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
