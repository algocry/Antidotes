import requests

def transmitter(message, base_url):
    dest_url = base_url + '/login.php'
    headers = {
        'Host': base_url,
        'User-Agent': 'Guess what?',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }

    cookies = {}

    data = 'username='+message+'&password= '

    response = requests.post('https://' + dest_url, headers=headers, data=data)
    return response.status_code

