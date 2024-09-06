# DESAFIO – Modificando arquivo html
from pathlib import Path

pasta_atual = Path(__file__).parent

item_remover = 'Beber suco'

with open(pasta_atual / 'index_desafio_01.html') as html:
    linhas_html = html.readlines()


nova_linhas_html = []
escrever_linha = True
for i, linha in enumerate(linhas_html):

    if i < len(linhas_html) - 3 and item_remover in linhas_html[i + 2]:
        escrever_linha = False

    if escrever_linha:
        nova_linhas_html.append(linha)
        # print(i, linha)

    if '</li>' in linha:
        escrever_linha = True


with open(pasta_atual / 'index_01.html', mode='w') as html:
    html.writelines(nova_linhas_html)

print('Processo finalizado!!')
