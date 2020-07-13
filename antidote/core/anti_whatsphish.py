import requests

def transmitter(message, base_url):
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
    data='number=' + str(message)
    try:
        response = requests.post('http://' + base_url + '/post.php', headers=headers, data=data)
    except:
        response = requests.post('https://' + base_url + '/post.php', headers=headers, data=data)
    return response.status_code
#print('http://' + base_url + '/post.php')
