from pathlib import Path

# Criar um objeto Path
path = Path(
    r'C:\Users\sergi\OneDrive\Documentos\ASIMOV ACADEMY\Python office\Lendo_Escrevendo_arquivos\file.txt')


# Obter informações sobre o arquivo
print(path.name)     # 'file.txt'
print(path.stem)     # 'file'
print(path.suffix)   # '.txt'
print(path.is_file())  # True


# Realizar operações com arquivos


path.write_text('Hellooo, World!')
content = path.read_text()
print(content)
path.rename('arquivo.txt')
# Remove (deleta) o arquivo
path.unlink()


# for nome in ['1file.txt', '2file.txt', '3file.txt']:
#     caminho_arquivo = caminho / nome
#     print(caminho_arquivo)

caminho_completo = Path(
    r'C:\Users\sergi\OneDrive\Documentos\ASIMOV ACADEMY\Python office\Lendo_Escrevendo_arquivos')


for nome in ['1file.txt', '2file.txt', '3file.txt']:
    caminho_file = caminho_completo / nome
    print(caminho_file)
