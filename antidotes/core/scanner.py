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
    SAYTHANKS = 'https://github.com/kennethreitz/saythanks.io'

def response_method(url):
    try:
        response = requests.get('https://' + url, headers=basic_headers,verify=False)
    except:
        response = requests.get('http://' + url, headers=basic_headers, verify=False)
    return response
    
def scan_cheese(url):
    response = response_method(url)
    if scan_keys.SAYCHEESE in response.text:
        return True
    else:
        return False

def scan_whatphish(url):
    response = response_method(url)
    if scan_keys.WHATPHISH in response.text:
        return True
    else:
        return False

def scan_shellphish(url):
    response = response_method(url)
    if scan_keys.SHELLPHISH in response.text:
        return True
    else:
        return False

def scan_zshadow(url):
    response = response_method(url)
    if scan_keys.ZSHADOW in response.text:
        return True
    else:
        return False

def scan_saythanks(url):
    response = response_method(url)
    if scan_keys.SAYTHANKS in response.text:
        return True
    else:
        return False
'''
url = 'https://saythanks.io/to/0x0is1off@gmail.com'
url = url.split('/')[2]

print(scan_cheese(url))'''