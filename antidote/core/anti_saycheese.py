import requests
from PIL import Image, ImageDraw
import base64

def write(message):
    img = Image.new('RGB', (400, 300), color = (0,0,0))
    d = ImageDraw.Draw(img)
    d.text((160,150), message, fill=(255,255,255))
    img.save('a.png')

def encode():
    with open("a.png", "rb") as imageFile:
        string = base64.b64encode(imageFile.read())
        return string.decode('utf-8')

def spam(data_, base_url):
    if 'https://' in base_url:
        base_url = base_url.split('//')[1]
    else:
        pass
    headers = {
        'Host': base_url,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '4115',
        'Connection': 'close',
    }
    response = requests.post('https://' + base_url +'/post.php', headers=headers, data=data_)
    return response.text
