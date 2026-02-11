import os
import django
import requests
import flask
import jinja2
import numpy as np
import pandas as pd
import yaml
import cryptography
import aiohttp
import urllib3
import paramiko
import celery
import httplib2
import PIL.Image
import rsa
import scipy
import sqlparse
import werkzeug

def check_vulnerable_versions():
    """
    This script simply imports and prints versions of libraries
    that are known to have security vulnerabilities in the 
    accompanying requirements.txt file.
    """
    print(f"Django version: {django.get_version()}")
    print(f"Requests version: {requests.__version__}")
    print(f"Flask version: {flask.__version__}")
    print(f"Jinja2 version: {jinja2.__version__}")
    print(f"PyYAML version: {yaml.__version__}")
    print(f"Cryptography version: {cryptography.__version__}")
    
    # Example of a transitive/dependency risk call
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://httpbin.org/robots.txt')
    print(f"Urllib3 status: {r.status}")

if __name__ == "__main__":
    check_vulnerable_versions()
    print("\n--- 20+ SCA Vulnerabilities Loaded in Manifest ---")
