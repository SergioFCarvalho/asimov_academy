# Exercício com planilha - independente do curso asimov

from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

# Lendo tabelas com DataFrame
tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx')  # caminho da planilha
# print(tb_vendas.head(5))

# Lendo aba específica da planilha (SP, MG, RJ)

uf = "SP"

tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx', sheet_name=uf)

# print(tb_vendas.head(5))

# Modificando Header -- padrão header = 0

tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx', sheet_name=uf, header=1)
# print(tb_vendas.head(5))


# Adicionando coluna index - index_col=0
tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx', sheet_name=uf)
# print(tb_vendas.head(5))


# Lendo colunas específicas -- usecols = [0, 1] ou ="A:B"
tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx', sheet_name=uf, usecols=[0, 2])
# print(tb_vendas.head(5))


# Escrevendo planilha | criando copia - [to_excel]
tb_vendas = pd.read_excel(pasta_atual / 'Planilhas' /
                          'ex_praticar.xlsx', sheet_name='MG')

# tb_vendas.to_excel(pasta_atual / 'Planilhas' / 'copiaEx.xlsx')


# Escrevendo diversas abas da planilha

tb_vendas_sp = pd.read_excel(
    pasta_atual / 'Planilhas' / 'ex_praticar.xlsx', sheet_name='SP')
tb_vendas_mg = pd.read_excel(
    pasta_atual / 'Planilhas' / 'ex_praticar.xlsx', sheet_name='MG')

# with pd.ExcelWriter(pasta_atual / 'Planilhas' / 'Copia_exe.xlsx') as nova_planilha:
#     tb_vendas_sp.to_excel(nova_planilha, sheet_name='SP', index=False)
#     tb_vendas_mg.to_excel(nova_planilha, sheet_name='MG', index=False)
