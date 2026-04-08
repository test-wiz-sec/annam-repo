import django
import requests
import flask
import jinja2
import yaml
import cryptography
import aiohttp
import urllib3
import paramiko
import celery
import httplib2
import PIL.Image
import rsa
import sqlparse
import werkzeug


def check_vulnerable_versions():
    """
    Imports libraries with known CVEs for SCA scanning.
    Replace requirements.txt / Pipfile.lock and run:
      snyk test --file=Pipfile.lock   (no install needed)
      snyk test                        (after pip install)
    """
    print(f"Django: {django.get_version()}")
    print(f"Requests: {requests.__version__}")
    print(f"Flask: {flask.__version__}")
    print(f"Jinja2: {jinja2.__version__}")
    print(f"PyYAML: {yaml.__version__}")
    print(f"Cryptography: {cryptography.__version__}")
    print(f"urllib3: {urllib3.__version__}")
    print(f"sqlparse: {sqlparse.__version__}")
    print(f"werkzeug: {werkzeug.__version__}")


if __name__ == "__main__":
    check_vulnerable_versions()
    print("\n--- SCA Vulnerabilities loaded from manifest ---")
