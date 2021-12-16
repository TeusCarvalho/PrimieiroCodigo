# tenho que importa as bilbiotecas que vou usar
import forca
import adivinhacao

def escolhe_jogo():

    print("################################")
    print("****** Escolha o Seu Jogo ******")
    print("################################")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        print("Jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo de Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
