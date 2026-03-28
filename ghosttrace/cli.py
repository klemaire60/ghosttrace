import click
from ghosttrace.modules.web import dns_lookup, whois_lookup, http_headers_lookup
from ghosttrace.output.display import display_dns, display_whois, display_http

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
	display_dns(dns_lookup(domain))
	display_whois(whois_lookup(domain))
	display_http(http_headers_lookup(domain))

def main():
	cli()