import click
from ghosttrace.modules.web import dns_lookup, whois_lookup, http_headers_lookup

@click.group()
def cli():
	pass

@cli.command()
def version():
	click.echo("GhostTrace v0.1.0")

@cli.command()
@click.argument("domain")
def web(domain):
	"""Do a DNS, WHOIS and HTTP Headers scan on the provided domain"""
	print(f"Scanned domain: {domain}\n")
	print(f"===== DNS =====\n{dns_lookup(domain)}\n")
	print(f"===== WHOIS =====\n{whois_lookup(domain)}\n")
	print(f"===== HTTP HEADERS =====\n{http_headers_lookup(domain)}\n")

def main():
	cli()