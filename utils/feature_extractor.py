from urllib.parse import urlparse

def extract_features(url):

    parsed = urlparse(url)

    path = parsed.path

    features = {
        "url_length": len(url),
        "valid_url": 1 if parsed.scheme and parsed.netloc else 0,
        "at_symbol": url.count("@"),
        "sensitive_words_count": sum(
            word in url.lower()
            for word in [
                "login",
                "secure",
                "verify",
                "bank",
                "account",
                "update",
                "signin"
            ]
        ),
        "path_length": len(path),
        "isHttps": 1 if parsed.scheme == "https" else 0,
        "nb_dots": url.count("."),
        "nb_hyphens": url.count("-"),
        "nb_and": url.count("&"),
        "nb_or": url.count("|"),
        "nb_www": url.lower().count("www"),
        "nb_com": url.lower().count(".com"),
        "nb_underscore": url.count("_")
    }

    return features