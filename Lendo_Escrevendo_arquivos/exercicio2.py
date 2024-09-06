from pathlib import Path
import os


def retorno_tamanho(caminho):
    for folder in path.glob('*'):
        if folder.is_dir() and not folder.name.startswith('.'):
            tamanho_folder = 0
            for arquivo in folder.glob('**/*'):
                if arquivo.is_file():
                    tamanho_folder += os.path.getsize(arquivo)
            print(">", folder.name,
                  round(tamanho_folder / 1024 / 1024, 2), 'mb')


path = Path.home() / 'Documents'
retorno_tamanho(path)
