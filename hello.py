#!/usr/bin/env python3

"""O programa irá ler a linguagem configurada no ambiente
e irá exibir um 'Hello World' no idioma correspondente

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_BR
    ou
    No cmd, passar o seguinte valor:
    LANG=pt_BR python3 nome_do_arquivo

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"     # Dunder Version
__author__ = "Iago Cruz"  # Dunder Author
__license__ = "unlicense" # Dunder License

import os     # Ler variáveis do ambiente

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US":"Hello, World!",
    "pt_BR":"Olá, Mundo!",
    "it_IT":"Ciao, Mondo!",
    "fr_FR":"Bonjour, Monde!"
}


print(msg[current_language])


