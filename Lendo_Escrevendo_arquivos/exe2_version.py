from pathlib import Path
import os


def retorno_tamanho(caminho, profundidade=1, tamanho_linha=0):
    for folder in path.glob('*'):
        if folder.is_dir() and not folder.name.startswith('.'):
            tamanho_folder = 0
            for arquivo in folder.glob('**/*'):
                if arquivo.is_file():
                    tamanho_folder += os.path.getsize(arquivo)
            print("--" * tamanho_linha, folder.name,
                  round(tamanho_folder / 1024 / 1024, 2), 'mb')
            if profundidade > 1:
                retorno_tamanho(folder, profundidade-1, tamanho_linha+1)


path = Path.home() / 'Documents'
retorno_tamanho(path, profundidade=3)
