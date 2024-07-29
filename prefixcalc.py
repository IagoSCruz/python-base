#!/usr/bin/env python3
"""Calculadora Prefix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py mul 10 5
>> 50

prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = '0.1.0'


import sys
argumentos = sys.argv[1:]


if not argumentos:
    operacao = (input('Operação: '))
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    argumentos = [operacao, n1, n2]

elif len(argumentos) != 3:
    print('Argumentos inválidos!')
    print()
    print('Ex: `sum 5 5`')
    sys.exit(1)

operacao, *numeros = argumentos

operacoes_validas = ('sum', 'sub', 'mul', 'div')

if operacao not in operacoes_validas:
    print('Utilize apenas as operações válidas:\nsum\nsub\nmul\ndiv')
    sys.exit(1)

numeros_validos = []
for num in numeros:
    if not num.isdigit():
        print('Número inválido.')
#print(argumentos[chave] )