import os

# Retorna uma String contendo o caminho completo diretório atual.
os.getcwd()

# Retorna uma lista dos arquivos e pastas do diretório atual.
os.listdir()

# os.chdir() - Troca o diretório atual.
actual_dir = os.getcwd()
os.chdir('\\Users\\xxx\\xyxyxy\\xkykyx\\xk')
print(os.getcwd())
os.chdir(actual_dir)

# Cria uma pasta
os.mkdir('Past1')
# Renomeia arquivos e pastas
os.rename('Past1', 'Past2')
# Deleta arquivos
os.remove('file.txt')
# Delata Pastas
os.rmdir('Past2')

# Acessa o cmd e executa comando no Sistema Operacional
cmd = 'notepad'
os.system(cmd)
