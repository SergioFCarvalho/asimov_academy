# Organizando Arquivos por extensão
from pathlib import Path
import shutil
import datetime


pasta_atual = Path(__file__).parent

pasta_a_organizar = pasta_atual / 'arquivos_desordem'

pasta_organizada = pasta_atual / 'arquivos_organizados'

pasta_backups = pasta_atual / 'backups'

if pasta_organizada.exists():
    shutil.rmtree(pasta_organizada)

pasta_organizada.mkdir()

if not pasta_backups.exists():
    pasta_backups.mkdir()

for arquivos in pasta_a_organizar.glob('**/*'):
    if arquivos.is_file():
        pasta_organizada_c_ext = pasta_organizada / \
            arquivos.suffix.replace('.', '')
        if not pasta_organizada_c_ext.exists():
            pasta_organizada_c_ext.mkdir()
        shutil.copy(arquivos, pasta_organizada_c_ext)

# 2 parte config da pasta backups

nome_backup = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(pasta_backups / nome_backup, 'zip', pasta_organizada)
