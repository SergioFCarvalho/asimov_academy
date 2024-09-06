import pickle
from pathlib import Path

pasta_atual = Path(__file__).parent

# Salvando arquivo pickle
minha_lista = [0, 1, 2]
meu_dict = {'N': 5, 'I': 33}

with open(pasta_atual / 'pickles' / 'lista.pickle', 'wb') as p:
    pickle.dump(minha_lista, p)


with open(pasta_atual / 'pickles' / 'dict.pickle', 'wb') as p:
    pickle.dump(meu_dict, p)


# Lendo arquivo pickle
with open(pasta_atual / 'pickles' / 'dict.pickle', 'rb') as d:
    dict_lido = pickle.load(d)


with open(pasta_atual / 'pickles' / 'lista.pickle', 'rb') as l:
    list_lido = pickle.load(l)

print(type(dict_lido), '=>>', dict_lido)
print(type(list_lido), '=>>', list_lido)
print('---------------------------------')
# Salvando a instância de uma classe com pickle


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def quem_sou_eu(self):
        print(f'Eu me chamo {self.nome} e tenho {self.idade} anos')


inst_sergio = Pessoa('Sérgio', 33)
inst_sergio.quem_sou_eu()
print('---------------------------------')

with open(pasta_atual / 'pickles' / 'inst_sergio.pickle', 'wb') as f:
    pickle.dump(inst_sergio, f)

# Lendo a mesma instância

with open(pasta_atual / 'pickles' / 'inst_sergio.pickle', 'rb') as inst:
    inst_salva = pickle.load(inst)


inst_salva.quem_sou_eu()
