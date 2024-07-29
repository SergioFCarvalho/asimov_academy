import os
from datetime import datetime

# Concatenar string
os.path.join(os.getcwd(), 'pasta')

# Retorna apenas a última pasta do diretório
os.path.basename(os.getcwd())

# Separa caminho da pasta. Retorna ambos segregados.
os.path.split(os.getcwd())

# Retorna a raiz do diretório especificado.
os.path.dirname(os.getcwd())

# Retorna o tempo da última atualização do diretório
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)  # -> 1718310475.2330148

datetime.fromtimestamp(lt)  # (2024, 6, 13, 17, 27, 55,..)


# Pergunta se determinado caminho é um arquivo
os.path.isfile(curr_dir)  # False

# Pergunta se determinado caminho é uma pasta
os.path.isdir(curr_dir)  # True


