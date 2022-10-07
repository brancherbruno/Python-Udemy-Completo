# DOCUMENTAÇÃO - STRING METHODS
"""
Para saber se a minha variável pode ser convertida em um inteiro?

isdecimal()
isdigit()
isnumeric()

se eu informar o tipo de variável na pergunta, não vou poder fazer a checagem de conversão.

ex: valor = int(input(...

Então essas funções vão retornar se o valor da variável  informado pode ser convertida em um inteiro. Porém só retornará
TRUE se o valor da variável informada foi número, POSITIVO ee não for FLOAT.
exemplo abaixo
"""

# abaixo código que o professor pediu para colocar para resolver os valores de float

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

# código do professor vem até a linha 38
n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')

print(n1.isnumeric())
print(n2.isnumeric())

"""
if is_number(n1) and is_number(n2):
    n1 = float(n1)
    n2 = float(n2)
    print(n1+n2)
else:
    print('Não posso converter uma string em valor numérico.')
"""
# PORÉM podemos usar uma pequena gambia para poder verificar sem usar o if and else

try:
    n1 = float(n1)
    n2 = float(n2)
    print(n1 + n2)
except:
    print('Não posso converter uma string em valor numérico.')

