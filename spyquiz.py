#!/usr/bin/env python3.5

'''
SPY
'''

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

             \033[41mBem-vindo ao Desafio Hacker!\033[1;m
""")

def Menu1():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar

\033[31m1\033[1;m) Iniciar
\033[31m2\033[1;m) Sobre
\033[31m3\033[1;m) Dependências
\033[31m4\033[1;m) Permissões
\033[31m5\033[1;m) Níveis

\033[31mq\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		Bloco1()
	elif opcao1 == "2":
		Sobre()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		Permissao()
	elif opcao1 == "5":
		MudarPara()
	elif opcao1 == "q":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()

def Permissao():
	Apresentacao()
	print("\n[\033[1;32m*\033[1;m] Arquivos a serem aplicados as permissões.\n")
	sleep(3)
	os.system("ls | grep spyquiz.py | lolcat && ls | grep url.py | lolcat")
	sleep(3)
	print("\n[\033[1;32m*\033[1;m] Pronto, permissões aplicadas.")
	sleep(3)
	os.system("chmod +x spyquiz.py url.py")
	Menu1()

def MudarPara():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] Você deseja ir para que nível ?

\033[31m01\033[1;m) Nível - #1: Descriptografia
\033[31m02\033[1;m) Nível - #2: Leitura de codigo fonte (Programação)
\033[31m03\033[1;m) Nível - #3: Observe
\033[31m04\033[1;m) Nível - #4: QrCode
\033[31m05\033[1;m) Nível - #5: Coleta de Informações, Wordlist
\033[31m06\033[1;m) Nível - #6: Usando camadas
\033[31m07\033[1;m) Nível - #7: Estenografia
\033[31m08\033[1;m) Nível - #8: ASCII - Dec
\033[31m09\033[1;m) Nível - #9: Base64
\033[31m10\033[1;m) Nível - #10: Binário
\033[31m11\033[1;m) Nível - #11: Espectograma
\033[31m12\033[1;m) Nível - #12: Matemática
\033[31m13\033[1;m) Nível - #13: Leia o enunciado
\033[31m14\033[1;m) Nível - #14: Octal
\033[31m15\033[1;m) Nível - #15: Hexa
\033[31m16\033[1;m) Nível - #16: Reverse

\033[31mq\033[1;m) Voltar
""")
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "01":
		Bloco1()
	elif opcao1 == "02":
		Bloco2()
	elif opcao1 == "03":
		Bloco3()
	elif opcao1 == "04":
		Bloco4()
	elif opcao1 == "05":
		Bloco5()
	elif opcao1 == "06":
		Bloco6()
	elif opcao1 == "07":
		Bloco7()
	elif opcao1 == "08":
		Bloco8()
	elif opcao1 == "09":
		Bloco9()
	elif opcao1 == "10":
		Bloco10()
	elif opcao1 == "11":
		Bloco11()
	elif opcao1 == "12":
		Bloco12()
	elif opcao1 == "13":
		Bloco13()
	elif opcao1 == "14":
		Bloco14()
	elif opcao1 == "15":
		Bloco15()
	elif opcao1 == "16":
		Bloco16()
	elif opcao1 == "q":
		Menu1()
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		MudarPara()

def Instalacao():
	def ArchDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos os componentes...\n")
		sleep(3)
		os.system("sudo pacman -S --noconfirm sl git gimp curl lolcat audacity")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso.")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	def DebianDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos os componentes...\n")
		sleep(3)
		os.system("sudo apt install -y sl git gimp curl lolcat audacity")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso.")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Escolha sua distribuição atual para a instalação dos requisítos.

\033[31m1\033[1;m) Arch Linux & Derivados
\033[31m2\033[1;m) Debian & Derivados
\033[31m3\033[1;m) Voltar
\033[31m4\033[1;m) Sair
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
[\033[1;32m*\033[1;m] Nível - #1: Descriptografia
 ____________________________________________
|                                            |
|      23a37c7340995c9192471ce06ae4c3e8      |
|____________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
[\033[1;32m*\033[1;m] Nível - #2: Leitura de codigo fonte (Programação)
 ____________________________________________________________________________________________
|                                                                                            |
|      Iremos apresentar um código fonte, de uma página web específica que agente achou      |
|                                                                                            |
|      Você terá que encontra o login e senha para passar, e ir pro nível seguinte.          |
|____________________________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		def urlpy():
			os.system("./url.py")
			responder = input("\n\033[1;36mDigite a senha para continuar: \033[1;m")
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
[\033[1;32m*\033[1;m] Nível - #3: Observe

[\033[1;91m!\033[1;m] OBS: Esse nível requer que você tenha instalado as dependências!
Caso tenha instalado, prossiga, caso não tenha vá para a opção 3
 ________________________________________________________
|                                                        |
|      A senha está na animação do letreiro do trem      |
|________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Instalar as dependências
\033[31m4\033[1;m) Sair
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
[\033[1;32m*\033[1;m] Nível - #4: QrCode
 __________________________________________
|                                          |
|      QrCode = https://goo.gl/RRRy5T      |
|__________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
	lista = []
	i = 1
	print('''
[\033[1;32m*\033[1;m] Nível - #5: Coleta de Informações, Wordlist
 _________________________________________________
|                                                 |
|Robert D. Baker                                  |
|Namorada: Ketty                                  |
|Estilo de música: Eletronica                     |
|Cidade: Nova York                                |
|Nome da mãe: Marta                               |
|Nome do pai: Peterson                            |
|Coordenadas geográficas: 43,010354, -88,076145   |
|Telefone: 414-557-3179                           |
|Codigo da cidade: 55                  	          |
|Data de nascimento: 20 de julho, 1982            |
|Idade: 34 anos                                   |
|Signo: Leão                                      |
|Endereço de e-mail: robertdbaker@gmail.com       |
|Nome de usuário: bakerdr                         |
|MasterCard: 5159 6656 3798 1026                  |
|Vence em: 6/2018                                 |
|Nome do cachorro: titicozito                     |
|Empresa: Robotic Solution                        |
|Ocupação: Robotica                               |
|Altura: 1,75                                     |
|Peso: 78 Kg                                      |
|Tipo sanguíneo: B+                               |
|Cor favorita: Verde                              |
|Veículo: Ninja H2R                               |
|_________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	bruteforce = input("\033[1;36mOpção:\033[1;m ")
	if bruteforce == "1":
		responder = input("\n\033[1;36mColoque a quantidade de senhas que você deseja importar a sua wordlist (ex: 5):\033[1;m ")
		print("\n")
		print("[\033[1;91m!\033[1;m] OBS: Digite as senhas que possa ser a da vitima, de acordo com os dados informados acima.\033[1;m")
		while i <= int(responder):
			nomes_das_senhas = input("\n\033[1;36mSenha #\033[1;m"+ str(i) +": ")
			lista.append(nomes_das_senhas)
			if nomes_das_senhas == bruteforcepass:
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco6()
				break
			i += 1

		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
[\033[1;32m*\033[1;m] Nível - #6: Usando camadas
 ______________________________________________________
|                                                      |
|      O login e senha está no arquivo "pass.psd"      |
|______________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
[\033[1;32m*\033[1;m] Nível - #7: Estenografia
 _______________________________________________________
|                                                       |
|      A senha está dentro da imagem "spypass.png"      |
|_______________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
            input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
[\033[1;32m*\033[1;m] Nível - #8: ASCII - Dec
 ______________________________________________________________________________
|                                                                              |
|                           Ache a senha...                                    |
|                                                                              |
|      | (35) | (83) | (112) | (121) | (65) | (83) | (67) | (73) | (73) |      |
|______________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
[\033[1;32m*\033[1;m] Nível - #9: Base64
 ____________________________________________
|                                            |
|      YmFzZTY0LWRlY29kZS1zdWNjZXNzZnVs      |
|____________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
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
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
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
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #10: Binário
 ________________________________________________________
|                                                        |
|      01100100 01101001 01100110 01100110 01101001      |
|      01100011 01110101 01101100 01110100 00111111      |
|________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == Binario:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco11()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco10()
	elif opcao1 == "2":
		Bloco11()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco10()

def Bloco11():
	espectograma = "AO44F"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #11: Espectograma
 __________________________________________________________________________
|                                                                          |
|      Faça um espectograma no arquivo "hex.wav" para achar a resposta     |
|__________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == espectograma:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco12()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco11()
	elif opcao1 == "2":
		Bloco12()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco11()

def Bloco12():
	matematica = "6608"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #12: Matemática
 _________________________________________________________________________
|                            |                                            |
|      M + M + M = 1080      |      E + 3º Termo da PG (2,4,...) = I      |
|                            |                                            |
|      M + A + A = 1314      |      I + Log4 64=x                         |
|                            |____________________________________________|
|      A + T + T = 511       |                                            |
|                            | Dica:                                      |
|      A + T x M = E         |      print("Ache a resposta final :3")     |
|____________________________|____________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == matematica:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco13()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco12()
	elif opcao1 == "2":
		Bloco13()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco12()

def Bloco13():
	pass_binario = "01100101 01101101 01100010 01101001 01101110 01100001 01110010 01101001 01101111"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #13: Leia o enunciado
 ____________________________________________________
|                                                    |
|      A senha para o próximo nível é: embinario     |
|____________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == pass_binario:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			os.system(Limpar)
			Bloco14()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco13()
	elif opcao1 == "2":
		Bloco14()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco13()

def Bloco14():
	pass_octal = "157 143 164 141 154 145 165 155 141 144 154 303 247"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #14: Octal
 _______________________________________________________
|                                                       |
|      A senha para o próximo nível é: octaleumadlç     |
|_______________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == pass_octal:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco15()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco14()
	elif opcao1 == "2":
		Bloco15()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco14()

def Bloco15():
	pass_hexad = "74 61 5f 61 63 68 61 6e 64 6f 5f 66 61 63 69 6c 5f 6e 65 5f 6d 6f 6c 65 71 75 65"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #15: Hexa
 ______________________________________________________________________
|                                                                      |
|      A senha para o próximo nível é: ta_achando_facil_ne_moleque     |
|______________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == pass_octal:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			Bloco16()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco15()
	elif opcao1 == "2":
		Bloco16()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco15()

def Bloco16():
	reverse_words = "Essa ferramenta vai te ajudar muito ainda - espere so para voce ver"
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #16: Reverse
 _______________________________________________________________________________
|                                                                               |
|      ver voce para so espere - ainda muito ajudar te vai ferramenta Essa      |
|_______________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		responder = input("\n\033[1;36mResposta:\033[1;m ")
		if responder == reverse_words:
			print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
			input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
			os.system(Limpar)
			FimDoDesafio()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco16()
	elif opcao1 == "2":
		os.system(Limpar)
		FimDoDesafio()
	elif opcao1 == "3":
		os.system(Sair)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco16()

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
