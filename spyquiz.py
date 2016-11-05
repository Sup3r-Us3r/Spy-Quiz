#!/usr/bin/env python3.5
#By Sup3r-Us3r and M4GN4S3C

'''
SPY
'''
from time import sleep
import os

Trem = "HelpHelp!"

def Apresentacao():
    os.system("reset")
    print("""\033[35m

  ██████  ██▓███ ▓██   ██▓     █████   █    ██  ██▓▒███████▒
▒██    ▒ ▓██░  ██▒▒██  ██▒   ▒██▓  ██▒ ██  ▓██▒▓██▒▒ ▒ ▒ ▄▀░
░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   ▒██▒  ██░▓██  ▒██░▒██▒░ ▒ ▄▀▒░ 
  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   ░██  █▀ ░▓▓█  ░██░░██░  ▄▀▒   ░
▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   ░▒███▒█▄ ▒▒█████▓ ░██░▒███████▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▓  ░▒▒ ▓░▒░▒
░ ░▒  ░ ░░▒ ░     ▓██ ░▒░     ░ ▒░  ░ ░░▒░ ░ ░  ▒ ░░░▒ ▒ ░ ▒
░  ░  ░  ░░       ▒ ▒ ░░        ░   ░  ░░░ ░ ░  ▒ ░░ ░ ░ ░ ░   Versão: 2.3.5
      ░           ░ ░            ░       ░      ░    ░ ░    
                  ░ ░                              ░   \033[1;m

             [\033[1;32m*\033[1;m] Desafio Hacker.
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
	os.system("chmod +x url.py")
	CLogin = "100"
	CSenha = "security"
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
		if login == CLogin:
			if senha == CSenha:
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco3()
			else:
				print("[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
				Bloco2()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
	elif codigofonte == "2":
		Bloco3()
	elif codigofonte == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

def Bloco3():
	Apresentacao()
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
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		sleep(5)
		os.system("sl -a")
		responder = input("\033[36mResposta: \033[1;m")
		if responder == Trem:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			Bloco4()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
	elif opcao1 == "2":
		Bloco4()
	elif opcao1 == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

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
		Bloco3()
	else:
		ComandoNaoEncontrado()

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado;
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor;
		''')

def Bloco4():
	Apresentacao()
	metasploitqr = "metasploit.php"
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
		if responder == metasploitqr:
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

def Bloco5():
	Apresentacao()
	bruteforcepass = "bakerdr20071982"
	print('''
			[*] Nível - #5: Coleta de Informações:

Descubra a senha através das informação dadas:
 _________________________________________________
|                                                 |
|Robert D. Baker                                  |
|2219 Woodlawn Drive                              |
|New Berlin, WI 53151                             |
|Nome de solteira da mãe: Morton                  |
|Coordenadas geográficas: 43,010354, -88,076145   |
|Telefone: 414-557-3179                           |
|Codigo da cidade: 55                  	          |
|Data de nascimento: 20 de julho, 1982            |
|Idade: 34 anos de Idade                          |
|Signo: Touro                                     |
|Endereço de e-mail: robertdbaker@gmail.com       |
|Nome de usuário: bakerdr                         |
|MasterCard: 5159 6656 3798 1026                  |
|Vence em: 6/2018                                 |
|CVC2: 028                                        |
|Empresa: Cellophane Square                       |
|Ocupação: Medical transcriptionist               |
|Altura: (171 centímetros)                        |
|Peso 78 Kg                                       |
|Tipo sanguíneo B+                                |
|Cor favorita: Verde                              |
|Veículo: 2008 BMW 320                            |
|_________________________________________________|

1) Responder;
2) Pular;
3) Sair;
''')
	bruteforce = input("\033[1;36mOpção:\033[1;m ")
	if bruteforce == "1":
		responder = input("\033[1;36mResponder:\033[1;m ")
		if responder == bruteforcepass:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			FimDoDesafio()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco5()
	elif bruteforce == "2":
		FimDoDesafio()
	elif bruteforce == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()

def Sobre():
	Apresentacao()
	print('''

\033[41m[#] Sobre:\033[1;m

Nome do Programa:        SpyQuiz
Data de Criação:         04/11/2016
Versão:                  2.3.5
Desenvolvedores:         \033[31mSup3r-Us3r\033[1;m - \033[31mM4GN4S3C\033[1;m
Descrição:

Ferramenta desenvolvida com o propósito de testar seus conhecimentos
na área de Segurança da Informação/Programação.


\033[41m[#] Sup3r-Us3r\033[1;m

[YOUTUBE]: \033[32mhttps://goo.gl/0feBCh\033[1;m
[GITHUB]: \033[32mhttps://github.com/Sup3r-Us3r\033[1;m



\033[41m[#] M4GN4S3C\033[1;m

[GITHUB]: \033[32mhttps://magnasec.github.io\033[1;m

''')
	input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
	Menu1()


def FimDoDesafio():
	os.system("reset")
	print(''' \033[31m
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████  ██▀███      ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒   ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ▓██ ░▄█ ▒   ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄     ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░     ░░   ░    ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░   ░            ░ ░        ░     ░  ░   ░     
                                                              ░ \033[1;m
                                   !! FIM DO QUIZ !!

''')
	sleep(10)
	Sobre()
	Menu1()

Menu1()