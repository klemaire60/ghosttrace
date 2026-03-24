
import click
@click.group()
def cli():
	pass

@cli.command()
def version():
	click.echo("GhostTrace v0.1.0")

def main():
	cli()