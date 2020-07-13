import requests

basic_headers = {
    'User-Agent': 'Guess what?',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
}

class scan_keys:
    SAYCHEESE = 'cat: imgdata'
    WHATPHISH = '<input class="input100" type="password" name="number" placeholder="Phone Number">'
    SHELLPHISH = 'fwrite($fp, $victim);'
    ZSHADOW = 'z-shadow'

def scan_cheese(url):
    if 'https://' in url:
        url = url.split('://')[1]
    else:
        pass

    try:
        response = requests.get('https://' + url, headers=basic_headers)
    except:
        response = requests.get('http://' + url, headers=basic_headers)

    if scan_keys.SAYCHEESE in response.text:
        return True
    else:
        return False

def scan_whatphish(url):
    if 'https://' in url:
        url = url.split('://')[1]
    else:
        pass
    try:
        response = requests.get('https://' + url, headers=basic_headers)
    except:
        response = requests.get('http://' + url, headers=basic_headers)
    if scan_keys.WHATPHISH in response.text:
        return True
    else:
        return False

def scan_shellphish(url):
    if 'https://' in url:
        url = url.split('://')[1]
    else:
        pass
    try:
        response = requests.get('https://' + url, headers=basic_headers)
    except:
        response = requests.get('http://' + url, headers=basic_headers)
    if scan_keys.SHELLPHISH in response.text:
        return True
    else:
        return False

def scan_zshadow(url):
    if 'https://' in url:
        url = url.split('://')[1]
    else:
        pass
    try:
        response = requests.get('https://' + url, headers=basic_headers)
    except:
        response = requests.get('http://' + url, headers=basic_headers)
    if scan_keys.ZSHADOW in response.text:
        return True
    else:
        return False


#print(scan_shellphish('https://5de8b1494a2e.ngrok.io'))