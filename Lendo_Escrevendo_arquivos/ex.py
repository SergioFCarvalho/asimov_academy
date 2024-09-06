from pathlib import Path

# Criar um objeto Path
path = Path('/home/user/documents/file.txt')

# Obter informações sobre o arquivo
print(path.name)     # 'file.txt'
print(path.suffix)   # '.txt'
print(path.is_file())  # True

# Realizar operações com arquivos
path.write_text('Hello, World!')
content = path.read_text()
path.rename('new_file.txt')
path.unlink()  # Excluir o arquivo

# Trabalhar com diretórios
directory = Path('/home/user/documents')
directory.mkdir(exist_ok=True)  # Criar o diretório, se não existir
for item in directory.iterdir():
    print(item)


path.mkdir(exist_ok=False, parents=False)

# Criar um novo diretório
new_dir = Path('documents/new_folder')
new_dir.mkdir()

# Criar um novo diretório e seus diretórios pais, se necessário
deeper_dir = Path('documents/folder1/folder2')
deeper_dir.mkdir(parents=True, exist_ok=True)
path.rmdir()


# Remover um diretório vazio
empty_dir = Path('documents/empty_folder')
empty_dir.mkdir()
empty_dir.rmdir()
path.glob('*.txt')


documents_dir = Path('documents')

# Encontrar todos os arquivos .txt no diretório 'documents'
text_files = list(documents_dir.glob('*.txt'))
print(text_files)

# Encontrar arquivos .py em todo o diretório 'documents' e seus subdiretorios
py_files = list(documents_dir.rglob('*.py'))
print(py_files)
path.is_dir()


documents_dir = Path('documents')
file_path = Path('documents/file.txt')

# Verificar se é um diretório
if documents_dir.is_dir():
    print(f"{documents_dir} é um diretório")
else:
    print(f"{documents_dir} não é um diretório")

# Verificar se é um arquivo
if file_path.is_file():
    print(f"{file_path} é um arquivo")
else:
    print(f"{file_path} não é um arquivo")

"""Esses exemplos demonstram como usar os métodos mkdir(), rmdir(), glob(), rglob() e is_dir() do pathlib.Path. Espero que isso ajude a entender melhor como trabalhar com caminhos de arquivos e diretórios usando a biblioteca pathlib.
"""
