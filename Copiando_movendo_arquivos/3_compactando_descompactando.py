from pathlib import Path
import shutil
import os

pasta_atual = Path(__file__).parent
# Compactando

pasta_a_ser_compactada = pasta_atual

nome_arquivo = pasta_atual / 'Compactado'

# - 1 nome arquivo - 2 formato de compactação - 3 pasta que sera compactada
# -- shutil.make_archive(nome_arquivo, 'zip', pasta_a_ser_compactada)


# Descompactando
nome_arq = pasta_atual / 'Compactado.zip'
pasta_descompactada = pasta_atual / 'Descompactada📌'

# - 1 nome do arquivo -2 nome da pasta descompactada - 3 formato do arquivo
shutil.unpack_archive(nome_arq, pasta_descompactada, 'zip')
