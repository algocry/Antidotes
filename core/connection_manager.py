import requests

def connection_check():
    response = requests.get('https://example.com')
    if response.status_code == 200:
        return True
    else:
        return False