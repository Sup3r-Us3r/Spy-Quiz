#!/usr/bin/env python3.5

from time import sleep
import os

Sair = "reset && exit"
Limpar = "reset"

def Apresentacao():
    os.system(Limpar)
    print("""\033[35m

  ██████  ██▓███ ▓██   ██▓     █████   █    ██  ██▓▒███████▒
▒██    ▒ ▓██░  ██▒▒██  ██▒   ▒██▓  ██▒ ██  ▓██▒▓██▒▒ ▒ ▒ ▄▀░
░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   ▒██▒  ██░▓██  ▒██░▒██▒░ ▒ ▄▀▒░ 
  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   ░██  █▀ ░▓▓█  ░██░░██░  ▄▀▒   ░
▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   ░▒███▒█▄ ▒▒█████▓ ░██░▒███████▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▓  ░▒▒ ▓░▒░▒
░ ░▒  ░ ░░▒ ░     ▓██ ░▒░     ░ ▒░  ░ ░░▒░ ░ ░  ▒ ░░░▒ ▒ ░ ▒
░  ░  ░  ░░       ▒ ▒ ░░        ░   ░  ░░░ ░ ░  ▒ ░░ ░ ░ ░ ░   Versão: 3.3.5
      ░           ░ ░            ░       ░      ░    ░ ░    
                  ░ ░                              ░   \033[1;m

             [\033[1;32m*\033[1;m] Bem-vindo ao Desafio Hacker!
""")

def Menu1():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar

1) Iniciar
2) Sobre
3) Dependências
4) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		Bloco1()
	elif opcao1 == "2":
		Sobre()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()

def Instalacao():
	def ArchDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos os componentes...\n")
		sleep(3)
		os.system("sudo pacman -S sl git gimp")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso...")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	def DebianDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos os componentes...\n")
		sleep(3)
		os.system("sudo apt install -y sl git gimp")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso...")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Escolha sua distribuição atual para a instalação dos requisítos.

1) Arch Linux & Derivados
2) Debian & Derivados
3) Voltar
4) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		ArchDerivados()
	elif opcao1 == "2":
		DebianDerivados()
	elif opcao1 == "3":
		Menu1()
	elif opcao1 == "4":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()


def Bloco1():
	Apresentacao()
	print('''
     	  [\033[1;32m*\033[1;m] Nível - #1: Descriptografia:
 ______________________________________________
|                                              |
|      23a37c7340995c9192471ce06ae4c3e8        |
|______________________________________________|

1) Responder
2) Pular
3) Sair
''')
	descriptografia = input("\033[1;36mOpção:\033[1;m ")
	if descriptografia == "1":
		responder = input("\n\033[1;36mResposta: \033[1;m")
		if responder == "spyquiz":
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco2()
		else:
			print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco1()
	elif descriptografia == "2":
		Bloco2()
	elif descriptografia == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco1()

def Bloco2():
	os.system("chmod +x url.py")
	senhacorreta = "Penetration Tester's"
	Apresentacao()
	print('''
       [\033[1;32m*\033[1;m] Nível - #2: Leitura de codigo fonte (Promogração):

Iremos propor um código de fonte de uma página Web específica, nela você terá de encontra 
o Login e a Senha para ir para o próximo nível.

1) Responder
2) Pular
3) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		def urlpy():
			os.system("./url.py")
			responder = input("\n\033[1;36mDigite a Senha para continuar: \033[1;m")
			if responder == senhacorreta:
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco3()
			else:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				urlpy()
		urlpy()
	elif opcao1 == "2":
		Bloco3()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco2()

def Bloco3():
	Trem = "HelpHelp!"
	Apresentacao()
	print('''
			[\033[1;32m*\033[1;m] Nível - #3: Observação:

[\033[1;91m!\033[1;m] OBS: Esse nível requer que você tenha instalado os requisítos!
Caso tenha instalado, continue, caso não tenha há uma opção
de instalar os resquisítos.
___________________________________________________________
|                                                          |
|      A senha está na animação do letreiro do trem...     |
|__________________________________________________________|

1) Responder
2) Pular
3) Instalar os requisítos
4) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		print("\n[\033[1;32m*\033[1;m] ATENÇÃO, o Trem vai passar!")
		sleep(5)
		os.system("sl -a")
		responder = input("\n\033[1;36mSenha: \033[1;m")
		if responder == Trem:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco4()
		else:
			print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco3()
	elif opcao1 == "2":
		Bloco4()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco3()

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado.
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor.
		''')

def Bloco4():
	Apresentacao()
	metasploitqr = "metasploit.php"
	print('''
			[\033[1;32m*\033[1;m] Nível - #4: QrCode:
 ______________________________________________
|                                              |
|        QrCode = https://goo.gl/RRRy5T        |
|______________________________________________|

1) Responder
2) Pular
3) Sair
''')
	acharqrcode = input("\033[1;36mOpção:\033[1;m ")
	if acharqrcode == "1":
		responder = input("\n\033[1;36mResponder:\033[1;m ")
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
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco4()

def Bloco5():
	Apresentacao()
	bruteforcepass = "bakerdr20071982"
	print('''
			[\033[1;32m*\033[1;m] Nível - #5: Coleta de Informações:

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

1) Responder
2) Pular
3) Sair
''')
	bruteforce = input("\033[1;36mOpção:\033[1;m ")
	if bruteforce == "1":
		responder = input("\n\033[1;36mResponder:\033[1;m ")
		if responder == bruteforcepass:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco6()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco5()
	elif bruteforce == "2":
		Bloco6()
	elif bruteforce == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco5()

def Sobre():
	Apresentacao()
	print('''

\033[41m[#] Sobre:\033[1;m

Nome do Programa:        \033[32mSpy-Quiz\033[1;m
Data de Criação:         \033[32m04/11/2016\033[1;m\033[1;m
Versão:                  \033[32m3.3.5\033[1;m
Desenvolvedores:         \033[32mSup3r-Us3r\033[1;m \033[41m-\033[1;m \033[32mM4GN4S3C\033[1;m


\033[41m[#] Descrição\033[1;m

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

def Bloco6():
	VLogin = "tecnologia"
	VSenha = "hacker"
	Apresentacao()
	print('''
       [\033[1;32m*\033[1;m] Nível - #6: Usando camadas...
 ______________________________________________
|                                              |
|   O login e senha está no arquivo pass.psd   |
|______________________________________________|

1) Responder
2) Pular
3) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		login = input("\n\033[1;32m[*] Login: \033[1;m")
		senha = input("\033[1;32m[*] Senha: \033[1;m")
		if login == VLogin:
			if senha == VSenha:
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco7()
			else:
				print("[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
				Bloco6()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco6()
	elif opcao1 == "2":
		Bloco7()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco6()

def Bloco7():
    estenografiapass = "spyquizestenografia"
    Apresentacao()
    print('''
       [\033[1;32m*\033[1;m] Nível - #7: A senha está na imagem
 __________________________________________________________________________
|                                                                          |
|        Estenografia é um processo de esconder senha em uma imagem        |
|__________________________________________________________________________|

1) Responder
2) Pular
3) Sair
''')
    opcao1 = input("\033[1;36mOpção:\033[1;m ")
    if opcao1 == "1":
        responder = input("\n\033[1;36mResposta:\033[1;m ")
        if responder == estenografiapass:
            print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
            input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
            Bloco8()
        else:
            print("[\033[1;91m!\033[1;m] Resposta incorreta.")
            input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
            Bloco7()
    elif opcao1 == "2":
        Bloco8()
    elif opcao1 == "3":
        os.system(Sair)
    else:
    	ComandoNaoEncontrado()
    	input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
    	Bloco7()

def Bloco8():
	ASCIISenha = "#SpyASCII"
	Apresentacao()
	print('''
			[\033[1;32m*\033[1;m] Nível - #8: Tabela ASCII - Dec.
 __________________________________________________________________________
|                                                                          |
|                           Ache a senha...                                |
|                                                                          |
|    | (35) | (83) | (112) | (121) | (65) | (83) | (67) | (73) | (73) |    |
|__________________________________________________________________________|

1) Responder
2) Pular
3) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == ASCIISenha:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco9()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco8()
	elif opcao1 == "2":
		Bloco9()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco8()

def Bloco9():
	Decode = "base64-decode-successful"
	Apresentacao()
	print('''
			[\033[1;32m*\033[1;m] Nível - #9: Descriptografia BASE64:
 __________________________________________________
|                                                  |
|                  Ache a senha...                 |
|                                                  |
|          YmFzZTY0LWRlY29kZS1zdWNjZXNzZnVs        |
|__________________________________________________|

1) Responder
2) Pular
3) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == Decode:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco10()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco9()
	elif opcao1 == "2":
		Bloco10()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco9()

def Bloco10():
	Binario = "difficult?"
	print('''
			[\033[1;32m*\033[1;m] Nível - #10: Binário
 __________________________________________________
|                                                  |
|                  Ache a senha...                 |
|                                                  |
|   01100100 01101001 01100110 01100110 01101001   |
|   01100011 01110101 01101100 01110100 00111111   |
|__________________________________________________|

1) Responder
2) Pular
3) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == Binario:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			FimDoDesafio()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
			Bloco10()
	elif opcao1 == "2":
		FimDoDesafio()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco10()

def FimDoDesafio():
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
	sleep(8)
	Sobre()
Menu1()