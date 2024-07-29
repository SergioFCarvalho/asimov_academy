def criar_tabuleiro():
    return [' ' for _ in range(9)]


def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        print(f"{tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]}")
        if i < 2:
            print("---------")


def resetar_tabuleiro():
    return [' ' for _ in range(9)]


def movimento_valido(tabuleiro, movimento):
    return tabuleiro[movimento] == ' '


def fazer_movimento(tabuleiro, movimento, jogador):
    if movimento_valido(tabuleiro, movimento):
        tabuleiro[movimento] = jogador
        return True
    return False


def verificar_vitoria(tabuleiro, jogador):
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for condicao in vitorias:
        if tabuleiro[condicao[0]] == tabuleiro[condicao[1]] == tabuleiro[condicao[2]] == jogador:
            return True
    return False


def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro


def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)
        movimento = int(
            input(f"Jogador {jogador_atual}, escolha uma posição (0-8): "))

        if fazer_movimento(tabuleiro, movimento, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                tabuleiro = resetar_tabuleiro()
                exibir_tabuleiro(tabuleiro)
                continue
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                tabuleiro = resetar_tabuleiro()
                exibir_tabuleiro(tabuleiro)
                continue
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Movimento inválido! Tente novamente.")


# Iniciar o jogo
jogo_da_velha()
