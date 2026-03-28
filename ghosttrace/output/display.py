from rich.console import Console
from rich.table import Table

console = Console()

def display_dns(data: dict):
	table = Table(title="DNS")
	table.add_column("Type", style="cyan")
	table.add_column("Valeur", style="white")

	for key, values in data.items():
		if values:
			for i, v in enumerate(values):
				label = str(key) if i == 0 else ""
				table.add_row(label, str(v))
		else:
			table.add_row(str(key), "none")
		
		table.add_section()

	console.print(table)

def display_whois(data: dict):
	table = Table(title="WHOIS")
	table.add_column("Champ", style="cyan")
	table.add_column("Valeur", style="white")

	for key, value in data.items():
		if isinstance(value, list):
			for i, v in enumerate(value):
				label = str(key) if i == 0 else ""
				table.add_row(label, str(v))
		else:
			table.add_row(str(key), str(value))
		table.add_section()

				
	table.add_section()

	console.print(table)

def display_http(data: dict):
	table = Table(title="HTTP Headers")
	table.add_column("Header", style="cyan")
	table.add_column("Valeur", style="white")

	for key, value in data["headers"].items():
		table.add_row(str(key), str(value))
		table.add_section()

	console.print(f"URL : {data["url"]}")
	console.print(f"PROTOCOL: [bold cyan]{data['protocol'].upper()}[/bold cyan]")
	console.print(f"STATUS : {data['status_code']}")
	console.print(table)
