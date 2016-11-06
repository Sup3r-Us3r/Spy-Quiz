#!/usr/bin/env python2
#coding: utf-8

from time import sleep
import urllib
import os

print """

 █    ██  ██▀███   ██▓          ██▓███ ▓██   ██▓
 ██  ▓██▒▓██ ▒ ██▒▓██▒         ▓██░  ██▒▒██  ██▒
▓██  ▒██░▓██ ░▄█ ▒▒██░         ▓██░ ██▓▒ ▒██ ██░
▓▓█  ░██░▒██▀▀█▄  ▒██░         ▒██▄█▓▒ ▒ ░ ▐██▓░
▒▒█████▓ ░██▓ ▒██▒░██████▒ ██▓ ▒██▒ ░  ░ ░ ██▒▓░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ 
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░ ░▒  ░▒ ░     ▓██ ░▒░ 
 ░░░ ░ ░   ░░   ░   ░ ░    ░   ░░       ▒ ▒ ░░  
   ░        ░         ░  ░  ░           ░ ░     
                            ░           ░ ░    

"""
sleep(3)


try:
    url = "http://www.100security.com.br/wargame/backtrack.php"
    os.system("clear")
    while True and not url.startswith("http://"):
        os.system("clear")
    else:
        print("Aguarde...")
        sleep(2)
        x = urllib.urlopen(url)
        print(x.read())
except KeyboardInterrupt:
    os.system("clear")
    print ("Control -C Pressionado fim do programa")

print """
|----------------------------------------------------------------------------|

[\033[1;32m*\033[1;m] Acima está o código-fonte, apenas ache a senha...

"""