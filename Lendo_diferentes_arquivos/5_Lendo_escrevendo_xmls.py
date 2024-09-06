# Lendo e Escrevendo Arquivos XML

import xml.dom.minidom
from pathlib import Path

pasta_atual = Path(__file__).parent

# Lendo arquivo xml
domtree = xml.dom.minidom.parse(str(pasta_atual / 'xmls' / 'livros.xml'))

group = domtree.documentElement
livros = group.getElementsByTagName('livro')
print(len(livros))

# Iterando por elementos e retornando valores
for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    # print('Titulo: ', titulo, '|', ' Autor: ', autor)

# Salvando um arquivo xml
livros[0].getElementsByTagName(
    'autor')[0].childNodes[0].nodeValue = 'Freire, Sergio'

with open(pasta_atual / 'xmls' / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)
