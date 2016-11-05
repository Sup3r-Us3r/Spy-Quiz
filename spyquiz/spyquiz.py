#!/usr/bin/env python3.5

from time import sleep
import os

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
[#] Desafio Hacker.
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
	Apresentacao()
	print('''
       [*] Nível - #2: Leitura de codigo fonte::

1) Responder;
2) Pular;
3) Sair;
''')
	codigofonte = input("\033[1;36mOpção:\033[1;m ")
	if codigofonte == "1":
		os.system("./url.py")
		login = input("\n\033[1;32m[*] Login: \033[1;m")
		senha = input("\033[1;32m[*] Senha: \033[1;m")
	if login == "100":
	if senha == "security":
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco3()
	else:
		print("[\033[1;91m!\033[1;m] Resposta incorreta.")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Bloco2()
	elif codigofonte == "2":
		Bloco3()
	elif codigofonte == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

def Bloco3():
	print('''
		[*] Nível - #3: Observação:

___________________________________________________________
|                                                          |
|      A senha está na animação do letreiro do trem...     |
|__________________________________________________________|

1) Responder;
2) Pular;
3) Sair;
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
[*] Escolha sua distribuição para a instalação do pacote sl:

1) Ubuntu & Debian
2) Arch Linux & Derivados
3) Já tenho o sl instalado
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
	elif distro == "3":
		print("Ok vamos prosseguir!")
		Bloco3()
	else:
		ComandoNaoEncontrado()

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado;
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor;
		''')-

def Bloco4():
	print('''
			[*] Nível - #4: QrCode:

 ______________________________________________
|                                              |
|        QrCode = https://goo.gl/RRRy5T        |
|______________________________________________|

1) Responder;
2) Pular;
3) Sair;
''')
	acharqrcode = input("\033[1;36mOpção:\033[1;m ")
	if acharqrcode == "1":
		responder = input("\033[1;36mResponder:\033[1;m ")
		if responder == "metasploit.php":
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco5()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco4()
	elif acharqrcode == "2":
		Bloco5()
	elif acharqrcode == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()



	Menu1()


Menu1()