import random
import os

options = ["papel", "pedra", "tesoura"]
player = 0
computer = 0

print("==" * 25)
print("Bem vindo ao jogo - Papel, Pedra e tesoura")


def main_print():
    print("=" * 25)
    print("\nPlacar:")
    print(f"Você: {player}")
    print(f"Computador: {computer}")
    print("\n")
    print("Escolha seu lance:")
    print("0 - Papel🖐️ | 1 - Pedra🤛 | 2 - Tesoura✌️")


def select_move():
    return random.choice(options)


def jogada():
    while True:
        try:
            minha_jogada = int(input())
            if minha_jogada not in [0, 1, 2]:
                raise
            return options[minha_jogada]
        except Exception as e:
            print(e)


def movimento_vencedor(jogador, computador):
    global player, computer

    if jogador == "papel":
        if computador == "pedra":
            player += 1
            return "p"
        elif computador == "tesoura":
            computer += 1
            return "c"
        else:
            return "d"

    if jogador == "tesoura":
        if computador == "papel":
            player += 1
            return "p"
        elif computador == "pedra":
            computer += 1
            return "c"
        else:
            return "d"

    if jogador == "pedra":
        if computador == "tesoura":
            player += 1
            return "p"
        elif computador == "papel":
            computer += 1
            return "c"
        else:
            return "d"


again = 1
while again == 1:
    main_print()
    meu_lance = jogada()
    lance_computador = select_move()
    vencedor = movimento_vencedor(meu_lance, lance_computador)

    print("")
    print("============================================")
    print(f"Sua jogada: {meu_lance.upper()}")
    print(f"Jogada do computador: {lance_computador.upper()}")

    if vencedor == "p":
        print("Você venceu!!!")
    elif vencedor == "c":
        print("Você perdeu!!!")
    else:
        print("Empate!!")
    print("============================================")

    while True:
        print("Jogar novamente? 0 - SIM | 1 - NÃO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break

    os.system("cls")
