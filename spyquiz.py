#!/usr/bin/env python3.5

from time import sleep
import os

CLogin = "100"
CSenha = "security"
Trem = "HelpHelp!"


def Apresentacao():
    os.system("reset")
    print("""

  ██████  ██▓███ ▓██   ██▓     █████   █    ██  ██▓▒███████▒
▒██    ▒ ▓██░  ██▒▒██  ██▒   ▒██▓  ██▒ ██  ▓██▒▓██▒▒ ▒ ▒ ▄▀░
░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   ▒██▒  ██░▓██  ▒██░▒██▒░ ▒ ▄▀▒░ 
  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   ░██  █▀ ░▓▓█  ░██░░██░  ▄▀▒   ░
▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   ░▒███▒█▄ ▒▒█████▓ ░██░▒███████▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▓  ░▒▒ ▓░▒░▒
░ ░▒  ░ ░░▒ ░     ▓██ ░▒░     ░ ▒░  ░ ░░▒░ ░ ░  ▒ ░░░▒ ▒ ░ ▒
░  ░  ░  ░░       ▒ ▒ ░░        ░   ░  ░░░ ░ ░  ▒ ░░ ░ ░ ░ ░
      ░           ░ ░            ░       ░      ░    ░ ░    
                  ░ ░                              ░   
[#] Desafio Hacker;
""")

def Menu1():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;

1) Iniciar;
2) Sobre;
3) Sair;
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		Iniciar()
	elif opcao1 == "2":
		Sobre()
	elif opcao1 == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

def Iniciar():
	Apresentacao()
	print('''
       [*] Nível - #1: Descriptografia:
 ______________________________________________
|                                              |
|      23a37c7340995c9192471ce06ae4c3e8        |
|______________________________________________|

1) Responder;
2) Pular;
3) Sair;
''')
	descriptografia = input("\033[1;36mOpção:\033[1;m ")
	if descriptografia == "1":
		responder = input("\033[1;36mResponder:\033[1;m ")
		if responder == "spyquiz":
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco2()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Iniciar()
	elif descriptografia == "2":
		Bloco2()
	elif descriptografia == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

def Bloco2():
	print('''
		[*] Nível - #2: Programação:
''')
	morebloco2 = "./url.py"
	os.system(morebloco2)
	login = input("\n\033[1;32m[*] Login: \033[1;m")
	senha = input("\033[1;32m[*] Senha: \033[1;m")
	if login == CLogin:
		if senha == CSenha:
			Distro()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
	else:
		print("[\033[1;91m!\033[1;m] Resposta incorreta.")

def Bloco3():
	print('''
		[*] Nível - #2: Observação:

A senha está na animação do letreiro do trem...

''')
	input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
	sleep(5)
	os.system("sl -a")
	responder = input("Resposta: ")
	if responder == Trem:
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
	else:
		print("[\033[1;91m!\033[1;m] Resposta incorreta.")

def Distro():
	print('''
[*] Escolha sua distribuição para a instalação do complemento:

1) Ubuntu & Debian;
2) Arch Linux & Derivados;
''')
	distro = input("\033[1;36mOpção:\033[1;m ")
	if distro == "1":
		os.system("sudo apt-get install -y sl")
		print("Instalado com Sucesso!")
		Bloco3()
	elif distro == "2":
		os.system("sudo pacman -Sy sl")
		print("Instalado com Sucesso!")
		Bloco3()
	else:
		ComandoNaoEncontrado()

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado;
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor;
		''')
	Menu1()


Menu1()