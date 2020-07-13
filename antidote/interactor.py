
# More modules to be added

import sys
from .core import scanner
from .core import connection_manager
from .core import anti_whatsphish
from .core import anti_shellphish
from .core import anti_saycheese
from .core import anti_zshadow


class scan_status:
    SHELLPHISH = False
    WHATPHISH = False
    SAYCHEESE = False
    ZSHADOW = False


class bcolors:
    HEADER = '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def scan(url):
    # saycheese
    print(bcolors.BOLD + bcolors.HEADER +
          'Scanning for saycheese...' + bcolors.ENDC)
    cheese_positive = scanner.scan_cheese(url)

    if cheese_positive:
        print(bcolors.BOLD + bcolors.OKGREEN +
              '[+] Found positive to saycheese' + bcolors.ENDC)
        scan_status.SAYCHEESE = True
    else:
        print(bcolors.BOLD + bcolors.FAIL +
              '[-] Found negative to saycheese' + bcolors.ENDC)
        scan_status.SAYCHEESE = False

    # shellphish
    print(bcolors.BOLD + bcolors.HEADER +
          'Scanning for shellphish...' + bcolors.ENDC)
    shellphish_positive = scanner.scan_shellphish(url)

    if shellphish_positive:
        print(bcolors.BOLD + bcolors.OKGREEN +
              '[+] Found positive to shellphish' + bcolors.ENDC)
        scan_status.SHELLPHISH = True

    else:
        print(bcolors.BOLD + bcolors.FAIL +
              '[-] Found negative to shellphish' + bcolors.ENDC)
        scan_status.SHELLPHISH = False

    # whatphish
    print(bcolors.BOLD + bcolors.HEADER +
          'Scanning for whatphish...' + bcolors.ENDC)
    whatsphish_positive = scanner.scan_whatphish(url)

    if whatsphish_positive:
        print(bcolors.BOLD + bcolors.OKGREEN +
              '[+] Found positive to whatphish' + bcolors.ENDC)
        scan_status.WHATPHISH = True
    else:
        print(bcolors.BOLD + bcolors.FAIL +
              '[-] Found negative to whatphish' + bcolors.ENDC)
        scan_status.WHATPHISH = False

    # zshadow
    print(bcolors.BOLD + bcolors.HEADER +
          'Scanning for zshadow...' + bcolors.ENDC)
    zshadow_positive = scanner.scan_zshadow(url)

    if cheese_positive:
        print(bcolors.BOLD + bcolors.OKGREEN +
              '[+] Found positive to zshadow' + bcolors.ENDC)
        scan_status.ZSHADOW = True
    else:
        print(bcolors.BOLD + bcolors.FAIL +
              '[-] Found negative to zshadow' + bcolors.ENDC)
        scan_status.ZSHADOW = False


def actions(url):
    if scan_status.SAYCHEESE:
        while True:
            message = input(bcolors.BOLD + bcolors.WARNING +
                            'Your Message> ' + bcolors.ENDC)
            time = int(input(bcolors.BOLD + bcolors.OKBLUE +
                             'Enter the number of times you want to show the same message: ' + bcolors.ENDC))
            anti_saycheese.write(message)
            data = 'cat=data:image/octet-stream;base64,' + \
                str(anti_saycheese.encode())
            for i in range(time):
                print(bcolors.BOLD + bcolors.OKBLUE +
                      'Sending [' + str(i) + ']' + bcolors.ENDC)
                try:
                    print(anti_saycheese.spam(data, url))
                    print(bcolors.BOLD + bcolors.OKGREEN +
                          '[+] Done..' + bcolors.ENDC)
                except Exception as e:
                    print(bcolors.BOLD + bcolors.FAIL +
                          '[-] Failed..' + bcolors.ENDC)
                    print(e)
        print()

    elif scan_status.SHELLPHISH:
        while True:
            message = input(bcolors.BOLD + bcolors.WARNING +
                            'Your Message> ' + bcolors.ENDC)
            if 'exit' not in message:
                break
            else:
                print(bcolors.BOLD + bcolors.OKBLUE +
                      'Sending [+]' + bcolors.ENDC)
                status_code = anti_shellphish.transmitter(message, url)
                if status_code == 200:
                    print(bcolors.BOLD + bcolors.OKGREEN +
                          '[+] Done..' + bcolors.ENDC)
                else:
                    print(bcolors.BOLD + bcolors.FAIL +
                          '[-] Failed..' + bcolors.ENDC)

            print()

    elif scan_status.WHATPHISH:
        while True:
            message = input(bcolors.BOLD + bcolors.WARNING +
                            'Your Message> ' + bcolors.ENDC)
            if 'exit' in message:
                break
            else:
                print(bcolors.BOLD + bcolors.OKBLUE +
                      'Sending [+]' + bcolors.ENDC)
                status_code = anti_whatsphish.transmitter(message, url)
                if status_code == 200:
                    print(bcolors.BOLD + bcolors.OKGREEN +
                          '[+] Done..' + bcolors.ENDC)
                else:
                    print(bcolors.BOLD + bcolors.FAIL +
                          '[-] Failed..' + bcolors.ENDC)
            print()

    elif scan_status.ZSHADOW:
        url = url.split('//')[1].split('/')[0]
        while True:
            message = input(bcolors.BOLD + bcolors.WARNING +
                            'Your Message> ' + bcolors.ENDC)
            if 'exit' not in message:
                break
            else:
                print(bcolors.BOLD + bcolors.OKBLUE +
                      'Sending [+]' + bcolors.ENDC)
                status_code = anti_zshadow.transmitter(message, url)
                if status_code == 200:
                    print(bcolors.BOLD + bcolors.OKGREEN +
                          '[+] Done..' + bcolors.ENDC)
                else:
                    print(bcolors.BOLD + bcolors.FAIL +
                          '[-] Failed..' + bcolors.ENDC)
            print()

    else:
        print(bcolors.BOLD + bcolors.FAIL +
              '[-] This Seems safe.' + bcolors.ENDC)


def main():
    banner_pre = bcolors.BOLD + 'Internet Check: ' + bcolors.ENDC
    try:
        x = connection_manager.connection_check()
        print(banner_pre + bcolors.BOLD + bcolors.OKGREEN +
              'Available' + bcolors.ENDC.join(''))
        print()

        try:
            url = input(bcolors.BOLD + bcolors.OKBLUE +
                        '[*] Enter URL to scan:' + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.OKBLUE +
                  '[*] Scanning started...' + bcolors.ENDC)
            scan(url)
            print(bcolors.BOLD + bcolors.OKBLUE + '[*] Done' + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.OKBLUE +
                  'Action started...' + bcolors.ENDC)
            actions(url)
        except Exception as e:
            print(bcolors.BOLD + bcolors.FAIL +
                  'Invalid url!!!' + bcolors.ENDC)
            print(e)
            pass
    except:
        print(banner_pre + bcolors.BOLD + bcolors.FAIL +
              'Not Available.' + bcolors.ENDC)
        exit(0)


if __name__ == "__main__":
    try:
        if sys.argv[1] == '-v' or '--version':
            print(bcolors.BOLD + bcolors.WARNING +
                  'Antidote v0.1' + bcolors.ENDC)
            exit(0)
    except Exception as e:
        main()
