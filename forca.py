import random
def impirme_mensagem_de_abertura():
    print("***********************************************************************")
    print("                                                                       ")
    print("**********************Bem vindo ao jogo de Forca!**********************")
    print("                                                                       ")
    print("***********************************************************************")
def carregar_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return (palavra_secreta)

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual é a letra.: ")
    chute = chute.strip().upper()
    return (chute)

def marca_chute_correto(chute, letra_acertadas, palavra_secreta):
    posicao = 0
    for index,letra in enumerate(palavra_secreta):
        if (chute.upper() == letra.upper()):
            letra_acertadas[posicao] = letra
        posicao = posicao + 1
def imprimir_mensagem_vencedor():
    print('Parabéns,	você	ganhou!')
    print("					   ___________						")
    print("					  '._==_==_=_.'				 	    ")
    print("					 .-\\:		/-.		                ")
    print("					| (|:.	    |)|		                ")
    print("					 '-|:.		|-'			            ")
    print("					   \\::.	/		                ")
    print("						'::. .'				            ")
    print("						  )	(			                ")
    print("						_.'	'._					        ")
    print("				       '-------'					    ")
    
def impirmir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {} " .format(palavra_secreta))
    print("	  ______________________________		")
    print("	 /				                \		")
    print("	/				                 \		")
    print("//								  \/\	")
    print("\|		XXXX			XXXX      |	/	")
    print("	|		XXXX			XXXX      |/	")
    print("	|		XXX			     XXX      |		")
    print("	|							      |		")
    print("	\__				XXX			   __/		")
    print("		|\			XXX			 /  |		")
    print("		| |						|	|		")
    print("		| I  I  I  I  I  I  I  I    |	    ")
    print("		|  I  I  I	I  I  I	 I      |		")
    print("		\_				           _/		")
    print("		  \_					_/	    	")
    print("			\__________________/		    ")
 
 
def jogar():
    impirme_mensagem_de_abertura()
    palavra_secreta = carregar_palavra_secreta()
    inicializa_letras_acertadas(palavra_secreta)
    letra_acertadas = ["_" for letra in palavra_secreta]
    acertou = False
    enforcou = False
    erro = 0
    print(letra_acertadas)
    while (not acertou and not enforcou) :
        
        chute = pede_chute()      
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letra_acertadas,palavra_secreta)            
        else :
            erro += 1
        enforcou = erro == 6
        acertou = "_" not in letra_acertadas
        
            
        print(letra_acertadas)
    if (acertou):
        imprimir_mensagem_vencedor()
    else :
        impirmir_mensagem_perdedor(palavra_secreta)
        #print("jogando...")
    print("Fim do Jogo")

jogar()