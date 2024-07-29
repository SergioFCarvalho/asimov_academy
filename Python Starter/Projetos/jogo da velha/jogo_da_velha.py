import os
import random


class game:
    def __init__(self):
        self.reset()

    def exibir_tabuleiro(self):
        print("")
        print(
            "" + self.board[0][0] + " | " +
            self.board[0][1] + " | " + self.board[0][2]
        )
        print("-------------")
        print(
            "" + self.board[1][0] + " | " +
            self.board[1][1] + " | " + self.board[1][2]
        )
        print("-------------")
        print(
            "" + self.board[2][0] + " | " +
            self.board[2][1] + " | " + self.board[2][2]
        )

    def reset(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.done = ""

    def checar_vitoria_ou_empate(self):
        dict_win = {}

        for i in ["X", "O"]:
            # horizontais
            dict_win[i] = (
                self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (
                self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (
                self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            # verticais
            dict_win[i] = (
                self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (
                self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (
                self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            # diagonais
            dict_win[i] = (
                self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (
                self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "x"
            RED = "\033[31m"
            GREEN = "\033[32m"
            RESET = "\033[0m"
            print(f"{GREEN} Jogador X venceu !!{RESET}")
            return
        elif dict_win["O"]:
            self.done = "o"
            print(f"{RED} Jogador O venceu!!!{RESET}")
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != "":
                    c += 1
                    break
        if c == 0:
            self.done = "d"
            print("Empate!!")
            return

    def movimento_jogador(self):
        invalid_mov = True

        while invalid_mov:
            try:
                print("Digite a linha do lance:")
                x = int(input)

                print("Digite a coluna do lance:")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Coordenadas erradas.")
                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_mov = False
            self.board[x][y] = "X"

    def movimento_computador(self):
        list_mov = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != "":
                    list_mov.append((i, j))

            if len(list_mov) > 0:
                x, y = random.choice(list_mov)
                self.board = "O"


gaming = game()
gaming.exibir_tabuleiro()
next = 0
while next == 0:
    os.system("cls")
    gaming.exibir_tabuleiro()
    while gaming.done == "":
        gaming.movimento_jogador()
        gaming.movimento_computador()
        os.system("cls")
        gaming.exibir_tabuleiro()
        gaming.checar_vitoria_ou_empate()

    print("Digite 1 para sair ou qualquer tecla para jogar novamente:")
    next = int(input)
    if next == 1:
        break
    else:
        gaming.reset()
        next = 0
