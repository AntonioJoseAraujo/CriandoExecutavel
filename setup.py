import sys
import os
from cx_Freeze import setup, Executable


# Definir o que deve ser incluído na pasta final
arquivos = ['dados.txt', 'musicas/']
# Saida de arquivos
configuracao = Executable(
    script='app.py',
    icon='circulo.ico'
)
# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatizar o login deste site',
    author='Antonio Araujo',
    options={'build_exe': {
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)
