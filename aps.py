# Importação da biblioteca para poder salvar uma variavel dentro de um arquivo;
# O programa necessita de uma chave para poder fazer a substituição, essa chave é dada pelo usuário;
# Seu funcionamento é: pegar a variavel com o texto e tira a quantidade de caracteres que o usuário colocar,
# Após, isso, ele salvará em um arquivo que estará no mesmo diretório do programa.
# Para decifrar, o usuário passará a mesma senha que passou antes, para que o programa faça a sua conversão;
# Caso o usuário deseje sair do programa, ele digitará a palavra "fim"  e ele terminará a sua execução;

import pickle

print("\nBem vindo ao programa de criptografia")

print(60 * "-")

def cifraAscii(cifra):

    resultado = []

    for letter in cifra:

        i = ord(letter)-chaveFinal

        resultado.append(i)

        with open("textoCifrado.txt", "wb") as fp:

            pickle.dump(resultado, fp)


def decifraAscii(arquivo):

    textoDecifrado = ""

    for numeros in arquivo:

        i = int(numeros)

        i += chaveFinal

        i = chr(i)

        textoDecifrado = (textoDecifrado+i)

    print("\n Sua mensagem decifrada é: " + textoDecifrado, sep="")

    print(60 * "-")


while True:

    opcao = input("\n Digite uma das opções abaixo: \n \n 1 - Cifra da mensagem; \n \n 2 - Decifragem da mensagem; \n \n 'FIM' - Sair do programa; \n \n Digite: ")

    print(60 * "-")

    if opcao == '1':

        primeiroTexto =input('\n Digite a frase que deseja cifrar: ')

        chave = input('\n Digite a senha-chave da criptografia: ')

        listaChaves = []

        for letter in chave:

            key = ord(letter)

            listaChaves.append(key)

        concatenaLista = [str(i) for i in listaChaves]

        chaveFinal = int("".join(concatenaLista))

        cifraAscii(primeiroTexto)

        print("\n \n Seu texto foi encriptado com sucesso, ele está salvo no arquivo textoCifrado.txt, no mesmo local em que está salvo o programa.")

        print(60 * "-")

    elif opcao == '2':

        chave = input('\n Digite a chave para decifrar: ')

        listaChaves = []

        for letter in chave:

            key = ord(letter)

            listaChaves.append(key)

        concatenaLista = [str(i) for i in listaChaves]

        chaveFinal = int("".join(concatenaLista))

        with open('textoCifrado.txt', 'rb') as fp:

            lerArquivo = pickle.load(fp)

        decifraAscii(lerArquivo)

        print(60 * '-')

    elif opcao.upper() == 'FIM':

        print('\n \n Programa finalizado')

        print(60 * '-')

        break

    else:

        print("\n \n Digito invalido, digite um valor válido, por favor")

        print(60 * '-')
