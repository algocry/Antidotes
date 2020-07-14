import requests
def transmitter(message, base_url):

    headers = {
        'Host': 'saythanks.io',
        'User-Agent': 'guess what?',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '41',
        'Origin': 'https://saythanks.io',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
    }
    data = 'body=' + message+ '&byline=cypher-bot&submit='
    try:
        response = requests.post(base_url + '/submit', headers=headers, data=data, verify=False)
        return response.status_code
    except Exception as e:
        return 404
#print(transmitter('hello2', 'https://saythanks.io/to/0x0is1off@gmail.com'))
