import whois
from urllib.parse import urlparse
from datetime import datetime

def get_domain_age(url):

    try:
        domain = urlparse(url).netloc

        if domain.startswith("www."):
            domain = domain[4:]

        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:

            age_days = (datetime.now() - creation_date).days

            return age_days

        return None

    except Exception:
        return None