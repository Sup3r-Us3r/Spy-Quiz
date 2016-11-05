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
    url = "http://www.100security.com.br/wargame/tux.php"
    os.system("clear")
    while True and not url.startswith("http://"):
        os.system("clear")
        print("exemplo: http://", url)
        url = str(raw_input("Digite um site para ver o codigo fonte: "))
    else:
        print("Aguarde...")
        x = urllib.urlopen(url)
        print(x.read())
except KeyboardInterrupt:
    os.system("clear")
    print ("Control -C Pressionado fim do programa")