from pathlib import Path

pasta_atual = Path(__file__).parent

# Lendo arquivo forma não recomendada

lista_compras = open(pasta_atual / 'doc.txt')

print(lista_compras.read())

lista_compras.close()

# Lendo arquivo forma recomendada - mode = r

with open(pasta_atual / 'doc.txt') as doc:
    print(doc.read())


# Lendo linha a linha - mode = r

with open(pasta_atual / 'doc.txt') as doc2:
    linha = doc2.readline()
    while linha != '':
        print(linha, end='')
        linha = doc2.readline()

# Lendo todas as linhas - mode = r

with open(pasta_atual / 'doc.txt') as doc3:
    print(doc3.readlines())

# Escrevendo arquivos


def gerar_lista_compras_atualizada(path, itens_comprados):
    with open(pasta_atual / 'doc.txt') as lista_compras:
        itens_lista = lista_compras.readlines()

    with open(pasta_atual / 'lista_compras_atualizada.txt', mode='w') as lista_atualizada:
        lista_atualizada.write('Lista Atualizada \n \n')
        for item in itens_lista:
            if not item.replace('\n', '') in itens_comprados:
                lista_atualizada.write(item)


itens_comprados = ['Arroz', 'Carne', 'Tomate']
gerar_lista_compras_atualizada(pasta_atual, itens_comprados)


# Escrevendo linha a linha

itens_comprados = ['Arroz', 'Carne', 'Tomate']
with open(pasta_atual / 'doc.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_atualizados = []
for item in itens_lista:
    if not item.replace('\n', '') in itens_comprados:
        itens_atualizados.append(item)

with open('lista_compras_atualizadas2.txt', mode='w') as nova_lista:
    nova_lista.write('Lista de Compras \n \n')
    nova_lista.writelines(itens_atualizados)


# Acrescentando valores a um arquivo

novos_itens = ['banana', 'uva', 'morango']
itens_c_quebra = [f'\n{item}' for item in novos_itens]


with open('lista_compras_atualizadas2.txt', mode='a') as itens_novos:
    itens_novos.writelines(itens_c_quebra)
