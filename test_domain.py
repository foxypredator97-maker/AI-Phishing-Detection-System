import whois

domain = "google.com"

info = whois.whois(domain)

print(info)