from pathlib import Path

# Retornando caminho do diretório trabalho atual
print(Path.cwd())

# Esse caminho é absoluto ? True
print(Path.cwd().is_absolute())

# Retornando caminho da primeira pasta
print(Path('1_pasta'))

# Esse caminho é absoluto? False
print(Path('1_pasta').is_absolute())
# Transformando caminho em absoluto
print(Path.cwd() / '1_pasta')
print((Path.cwd() / '1_pasta').exists())

# Garantido que estamos retornando o caminho da pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)

print(Path(__file__).parent / '1_pasta')
print((Path(__file__).parent / '1_pasta').exists())
# Trabalhando com partes do caminho
caminho = Path(__file__)

print(caminho.parent)
print(caminho.name)
print(caminho.stem)
print(caminho.drive)
print(caminho.parents[0])
