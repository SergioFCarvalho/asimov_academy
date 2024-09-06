# OBS : pip install pandas | pip install openpyxl

from pathlib import Path
import pandas as pd


pasta_atual = Path(__file__).parent

# > Lendo tabelas com DataFrame

tabelas_clientes = pd.read_excel(pasta_atual / 'Planilhas' / 'clientes.xlsx')
# print(tabelas_clientes.head(10))


# > Lendo abas específicas

tabelas_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SP')
# print(tabelas_clientes.head(10))


# > Modificando Header -- padrão header = 0

tabelas_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SP', header=0)
# print(tabelas_clientes.head(5))


# Adicionando coluna index

tabelas_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SP', header=0, index_col=0)
# print(tabelas_clientes.head(8))

# Lendo colunas específicas -- usecols = [0, 1] ou ="A:B"

tabelas_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SC', usecols=[1, 2])
# print(tabelas_clientes.head(8))


# Comentários sobre decimais e thousands -- decimal = '.' | thousands = '.'

tabelas_clientes2 = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SP', decimal=".")
# print(tabelas_clientes2.head(5))


# Escrevendo planilha | criando copia

"""tb_clientes = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='PR')
tb_clientes.to_excel(pasta_atual / 'Planilhas' / 'copia_clientes.xlsx')"""

# Escrevendo diversas abas da planilha

tb_clientes_rs = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='RS')
tb_clientes_sc = pd.read_excel(
    pasta_atual / 'Planilhas' / 'clientes.xlsx', sheet_name='SC')

with pd.ExcelWriter(pasta_atual / 'Planilhas' / 'copia_clientes.xlsx') as nova_planilha:
    tb_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
    tb_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index=False)
