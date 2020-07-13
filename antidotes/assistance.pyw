import sys
import pyperclip
import notify2 
from .core import scanner

scan_status = {}

clip = {1: ""}

notify2.init("Antidote's URL notifier")
safe = notify2.Notification("Safe URL", "This URL is safe from top malicious stuff.")
danger = notify2.Notification("Malicious URL detected", "This URL is is detected malicious. You should run 'interator' to scan this")

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def simple_scan(url):
    try:
        if 'https://' or 'http://' in url:
            url = url.split('/')[2]
        if not '/' in url:
            pass
        else:
            url = url.split('/')[0]
    except:
        pass
    scan_status[1] = str(scanner.scan_cheese(url))
    scan_status[2] = str(scanner.scan_shellphish(url))
    scan_status[3] = str(scanner.scan_whatphish(url))
    scan_status[4] = str(scanner.scan_zshadow(url))

if __name__ == "__main__":
    while True:
        clip[2] = pyperclip.paste()
        if clip[2] != clip[1]:
            clip[1] = clip[2]
        else:
            continue
        if clip[1] != "":
            if \
            'http' or 'https' or '.com' or '.net' or '.io' \
            or '.org' or 'ftp' or 'smtp' or '.us' or '.uk' or '.ai' \
            or '.uk' or '.in' or '.mobi' or '.ngrok' or 'serveo.' \
            in clip[1]:
                try:
                    simple_scan(clip[1])
                except:
                    continue
            if 'True' in scan_status:
                danger.show()
            #    print(str(True) + clip[1])
            else:
                safe.show()
            #    print(str(False) + clip[1])
        else:
            pass