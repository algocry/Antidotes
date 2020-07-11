from bs4 import BeautifulSoup as scrapper
import requests

def bypass_human_verfication(base_url):
    #Making request to get victims id by passing human verification


    headers = {
            'Host': base_url,
            'User-Agent': 'Guess what?',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '30',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }
    data1 = 'shrtlink=guesswhat&submit=Submit'
    inits = base_url.split('?')

    try:
        response = requests.post(inits[0], headers=headers, data=data1)
    except Exception as e:
        return False
    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".

    try:
        response1 = requests.post(base_url, headers=headers, data=data1)
        return response1
    except Exception as e:
        return False

def get_user_id(base_url):
    #Obtaining user_id

    headers = {
            'Host': base_url,
            'User-Agent': 'Guess what?',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '30',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }
    response = bypass_human_verfication(base_url)

    if response != False:
        soup = scrapper(response.content, 'html.parser')
        try:
            victim_id = soup.find('input', {'name': 'user_id_victim'}).get('value')
            return victim_id
        except Exception as e:
            return False
    else:
        return False

def transmitter(base_url, message):
    #Making request to send spam credential to Hacker
    
    headers = {
            'Host': base_url,
            'User-Agent': 'Guess what?',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '30',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }
    victim_id = get_user_id(base_url)
    if victim_id != False:
        data = 'email='+ message +'&pass=noob&user_id_victim='+victim_id+'&type=a'
        try:
            response = requests.post('https://' + base_url +'/zs1.php', headers=headers, data=data)
            return response.status_code
        except Exception as e:
            return False
    else:
        return False