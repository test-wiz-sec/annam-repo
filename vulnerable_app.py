import requests
import flask
import pyyaml
import cryptography

# Vulnerable versions of dependencies used below
# requests==2.18.0  - CVE-2018-18074 (credential exposure)
# flask==0.12.2     - CVE-2018-1000656 (DoS via large JSON)
# pyyaml==3.13      - CVE-2017-18342 (arbitrary code execution via yaml.load)
# cryptography==2.1 - CVE-2018-10903 (weak key generation)

def fetch_data(url):
    response = requests.get(url)
    return response.text

def parse_config(yaml_string):
    # Unsafe yaml.load call - SCA finding: use yaml.safe_load instead
    import yaml
    return yaml.load(yaml_string)

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
