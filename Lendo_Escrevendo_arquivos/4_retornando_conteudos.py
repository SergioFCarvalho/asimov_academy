from pathlib import Path


# Listando arquivos de uma pasta
print(list(Path.cwd().glob('*')))
# Listando arquivos de uma determinada extensão
print(list(Path.cwd().glob('*.py')))
# Listando tudo dentro de uma pasta
print(list(Path.cwd().glob('**/*')))
# Validando caminhos
nao_exists = Path.home() / 'no_exists'
print(nao_exists.exists())
# Verificando se é arquivo ou pasta
print(Path(__file__).is_file())

dire = Path(__file__).parent
print(dire.is_file())
print(dire.is_dir())
