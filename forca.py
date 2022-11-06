import random

#Início

def jogar():
    logo()
    secret_word = carrega_palavra_secreta()
    word_rigth = started_words_right(secret_word)
    print(word_rigth)

    enforcou = False
    acertou = False
    attemps = 0

    while (not enforcou and not acertou):
        chut = chutes()

        if (chut in secret_word):
            chute_correto(chut, word_rigth, secret_word)
        else:
            attemps += 1
            draw_forca(attemps)

        enforcou = attemps == 7
        acertou = '_' not in word_rigth
        print(word_rigth)

    if (acertou):
        winnner()
    else:
        loser(secret_word)

#Fim

def logo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("***  Powered by Luís - Void   ***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    words = []

    for linha in arquivo:
        linha = linha.strip()
        words.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(words))
    secret_word = words[numero].upper()
    return secret_word


def started_words_right(word):
    return ["_" for letra in word]


def chutes():
    chut = input("Qual letra?")
    chut = chut.strip().upper()
    return chut


def chute_correto(chut, word_rigth, secret_word):
    index = 0
    for letra in secret_word:
        if (chut == letra):
            word_rigth[index] = letra
        index += 1

def winnner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("************************")
    print("Powered by Void")

def loser(secret_word):
    print("Puxa, você perdeu!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("***************************")
    print("Powered by Void")


def draw_forca(attemps):
    print("  _______     ")
    print(" |/      |    ")

    if(attemps == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(attemps == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(attemps == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(attemps == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(attemps == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(attemps == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attemps == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
