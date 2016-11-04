#!/usr/bin/env python3.5

#By Magno
#Date 04/11/2016

import os

def Apresentacao():
    print("""
    _,.---._                                  .=-.-.
  ,-.' - ,  `.           .--.-. .-.-.        /==/_ /         ,--,----.
 /==/ ,    -  \         /==/ -|/=/  |       |==|, |         /==/` - ./
|==| - .=.  ,  |        |==| ,||=| -|       |==|  |         `--`=/. /
|==|  : ;=:  - |        |==|- | =/  |       |==|- |          /==/- /
|==|,  '='  ,  |        |==|,  \/ - |       |==| ,|         /==/- /-.
 \==\ _   -    ;        |==|-   ,   /       |==|- |        /==/, `--`\ .=.
  '.='.  ,  ; -\        /==/ , _  .'        /==/. /        \==\-  -, |:=; :
    `--`--'' `--`       `--`..---'          `--`-`          `--`.-.--` `=`
""")

nome = input("Login: ")
passw = input("Senha: ")

print ("[\033[1;32m*\033[1;m] Bora lá", nome + "!")
os.system("clear")

def Menu():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Iniciar;
2) Sobre;
3) Sair;
''')

pergunta = input("Opção: ")
