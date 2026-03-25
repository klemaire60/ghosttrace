import dns.resolver
import whois
import httpx

def dns_lookup(domain):
	DNS_saves = {
		"A" : [],
		"MX" : [],
		"NS": [],
		"TXT": []
	}
	resolver = dns.resolver.Resolver()

	for key in DNS_saves:
		try: 
			answers = resolver.resolve(domain, key)
			for rdata in answers:
				DNS_saves[key].append(str(rdata))
		except dns.resolver.NoAnswer:
			pass
		except dns.resolver.NXDOMAIN:
			pass
		except dns.resolver.Timeout:
			pass

	return DNS_saves

def whois_lookup(domain):
	data = {}
	try : 
		data = whois.whois(domain)
	except whois.WhoisError:
		pass
	except Exception:
		pass
	
	keys = ["domain_name", "registrar", "creation_date", "expiration_date", "name_servers"]
	return {k: str(data.get(k,"none")) for k in keys}

def http_headers(domain):
    try:
        response = httpx.get("https://" + domain, timeout=5)
        protocol = "https"
    except (httpx.TimeoutException, httpx.ConnectError, httpx.InvalidURL):
        try:
            response = httpx.get("http://" + domain, timeout=5)
            protocol = "http"
        except httpx.TimeoutException:
            return {"error": "Timeout"}
        except httpx.InvalidURL:
            return {"error": "Invalid URL"}
        except httpx.ConnectError:
            return {"error": "Connection failed"}

    return {
        "url": str(response.url),
        "protocol": protocol,
        "status_code": response.status_code,
        "headers": dict(response.headers)
    }

if __name__ == "__main__":
	domain = "example.com"

	print('===== DNS =====')
	for items in dns_lookup(domain).items():
		print(items)

	print('===== WHOIS =====')
	for items in whois_lookup(domain).items():
		print(items)

	print('===== HTTP HEADERS =====')
	for items in http_headers(domain).items():
		print(items)