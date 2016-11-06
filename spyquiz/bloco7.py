	def Bloco7():
    estenografiapass = "spyquizestenografia"
	Apresentacao()
	print('''
       [*] Nível - #7: A senha está na imagem
 __________________________________________________________________________
|                                                                          |
|        Estenografia é um processo de esconder senha em uma imagem        |
|                                                                          |
|                      Download - https://goo.gl/NDL8aN                    |
|                                                                          |
|            Sistema utilizado para a estenografia "Arch Linux"            |
|__________________________________________________________________________|

1) Responder;
2) Pular;
3) Sair;
''')
	estenografia = input("\033[1;36mOpção:\033[1;m ")
	if estenografia == "1":
		responder = input("\033[1;36mResponder:\033[1;m ")
		if responder == estenografiapass:
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco8()
			else:
				print("[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
				Bloco7()
		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
	elif imagem == "2":
		Bloco8()
	elif imagem == "3":
		os.system("exit")
	else:
		ComandoNaoEncontrado()
