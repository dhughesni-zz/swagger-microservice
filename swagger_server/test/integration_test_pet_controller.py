import requests
from urllib.parse import urlencode

assert 200 == requests.get('http://0.0.0.0:5000/v2/pet/findByStatus', params = ({'status': ['available']})).status_code
assert 200 == requests.get('http://0.0.0.0:5000/v2/pet/findByStatus', params = ({'status': ['pending']})).status_code
assert 200 == requests.get('http://0.0.0.0:5000/v2/pet/findByStatus', params = ({'status': ['sold']})).status_code
assert 400 == requests.get('http://0.0.0.0:5000/v2/pet/findByStatus', params = ({'status': ['INVALID_OPTION']})).status_code
