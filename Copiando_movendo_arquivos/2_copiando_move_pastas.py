from pathlib import Path
import shutil

pasta_atual = Path(__file__).parent

# Criando pasta
caminho_pasta_destino = pasta_atual / 'destino4'

# --caminho_pasta_destino.mkdir(exist_ok=True)

# Criando pasta  com todos as pastas anteriores
caminho_pasta_destino = pasta_atual / 'destino5' / 'destino51'
# -- caminho_pasta_destino.mkdir(parents=True)

# Copiando pastas
caminho_pasta_destino = pasta_atual / 'destino5'
caminho_pasta_destinado = pasta_atual / 'destino1' / 'destino5'
# --shutil.copytree(caminho_pasta_destino, caminho_pasta_destinado)

# Deletando pastas vazias
pasta_remover = pasta_atual / 'destino5' / 'destino51'
# --pasta_remover.rmdir()

# Deletando pastas com conteúdo
pasta_remover = pasta_atual / 'destino1'
shutil.rmtree(pasta_remover)
