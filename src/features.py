import re
from urllib.parse import urlparse

import tldextract


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "confirm",
    "password",
]


def has_ip_address(url: str) -> int:
    pattern = r"(\d{1,3}\.){3}\d{1,3}"
    return int(bool(re.search(pattern, url)))


def count_digits(url: str) -> int:
    return sum(char.isdigit() for char in url)


def count_suspicious_keywords(url: str) -> int:
    url_lower = url.lower()
    return sum(keyword in url_lower for keyword in SUSPICIOUS_KEYWORDS)


def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    extracted = tldextract.extract(url)

    hostname = parsed.netloc
    path = parsed.path

    features = {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(path),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "slash_count": url.count("/"),
        "digit_count": count_digits(url),
        "has_https": int(parsed.scheme == "https"),
        "has_ip": has_ip_address(url),
        "subdomain_count": len(extracted.subdomain.split(".")) if extracted.subdomain else 0,
        "suspicious_keyword_count": count_suspicious_keywords(url),
    }

    return features