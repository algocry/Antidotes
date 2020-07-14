import requests

def connection_check(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False