#!/usr/bin/env python3

"""O programa irá ler a linguagem configurada no ambiente
e irá exibir um 'Hello World' no idioma correspondente

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"     # Dunder Version
__author__ = "Iago Cruz"  # Dunder Author
__license__ = "unlicense" # Dunder License

import os     # Ler variáveis do ambiente

current_language = os.getenv("LANG")[:5]

msg = 'Hello, World'

if current_language == 'pt_BR':
    msg = 'Olá, Mundo!'
elif current_language == 'it_IT':
    msg = 'Ciao, Mondo!'


print(msg)


