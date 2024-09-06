from pathlib import Path


# Localizador de arquivos
c = Path.cwd().parents[1]


def encontrar_arquivo(caminho, nome_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_arquivo:
                print(arquivo)


encontrar_arquivo(c, '1path')
