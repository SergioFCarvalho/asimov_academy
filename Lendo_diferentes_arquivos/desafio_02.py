# DESAFIO – Separando e Consolidando Planilhas

from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent


tabela_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name=None)

# criar a pasta planilha separadas
pasta_separada = (pasta_atual / 'Planilhas' / 'Planilha_separadas')
Path.mkdir(pasta_separada, parents=True, exist_ok=True)

# separa as abas da planilha em várias planilhas

for uf, tab in tabela_clientes.items():
    tab.to_excel(pasta_separada / f'{uf}.xlsx', index=False)


# Consolidando planilhas que foram separadas

# Criando pasta da planilha separada
pasta_consolidada = pasta_atual / 'Planilhas' / 'Planilha_consolidada'
pasta_consolidada.mkdir(parents=True, exist_ok=True)

# Escrevendo as abas em uma planilha
with pd.ExcelWriter(pasta_consolidada / 'nova_clientes.xlsx') as nova_planilha:
    for arquivos in Path(pasta_separada).glob('*.xlsx'):
        tabela = pd.read_excel(arquivos)
        tabela.to_excel(nova_planilha,
                        sheet_name=arquivos.stem, index=False)
