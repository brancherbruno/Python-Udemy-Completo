"""
DESEMPACOTAMENTO DE LISTAS
"""

nomes = ['Bruno', 'Renata', 'Rafaela']

n1, n2, n3 = nomes

print(n1, n2, n3)
print(n3)
print(n1)
print(n2)

print()
print('='*40)
print()

nome = ['BRUNO', 'RENATA', 'PEDRO', 1, 2, 3, 4, 5, 6, 7]

no1, no2, *outra_lista = nome

print(no1, no2, outra_lista)

