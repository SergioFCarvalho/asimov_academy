# Lendo e Escrevendo Json

import json
from pathlib import Path
# import sys
# sys.stdin.reconfigure(encoding="utf-8")

pasta_atual = Path(__file__).parent

data_json = '''
{
"assinantes": [
    {
    "nome": "Adriano peroni",
    "telefone": "51 99999999",
    "email": "adriano@email.com",
    "em_dia": true
    },
    {
    "nome": "Juliano faccioni",
    "telefone": "51 99999999",
    "email": "juliano@email.com",
    "em_dia": false
    }
],
"data_extração": "2023/08/22"
}
'''

# > Convertendo json para dicionário

dado_convertido = json.loads(data_json)

'''print(type(dado_convertido))
print(dado_convertido)'''

# > Convertendo novamente para json
dado_json = json.dumps(dado_convertido, ensure_ascii=False, indent=2)

'''print(type(dado_json))
print(dado_json)'''

# > Lendo arquivos json

with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
    arquivo_json = json.load(f)
    # print(json.load(f))

# > Escrevendo arquivos json
with open(pasta_atual / 'jsons' / 'copia_assinantes.json', 'w') as cp:
    json.dump(arquivo_json, cp, indent=2, ensure_ascii=False)
