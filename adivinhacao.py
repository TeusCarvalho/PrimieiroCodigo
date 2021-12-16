# tenho que importa as bilbiotecas que vou usar

import random
def jogar():
    print("################################")
    print("Bem vinda ao jogo de Advinhação!")
    print("################################")

    # Devo declarar as funçoes aqui embaixo
    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade!! ")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int (input("Defina Seu nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):  # Range parâmetro range( inico, para,[salto])
        print("Tentatativa {} de {}".format(rodada, total_tentativas)) #format deixar mais bonito
        chute_str = input("Digite um número de 1 a 100: ")
        chute = int(chute_str)
        print("Você Digitou ", chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # funçoes que estou usando
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você Acertou, e fez {} pontos!!".format(pontos))
            break  # Para o jogo
        else:
            if maior:
                print("Você Errou! O seu numero foi maior que o numero secreto.")
            elif menor:
                print("Você Errou! O seu numero foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #menos o numero do seu chute
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()
