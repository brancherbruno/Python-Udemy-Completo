'''
Split - dividir uma str

Join - juntar uma lista ou uma str

Enumerate - enumerar elementos de uma lisa
'''

string = 'O Brasil é o país do futebol, e o Brasil vai ser hexa em 2022'

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

print()

for valor in lista_1:
    print(valor)

print()

palavra = ''
cont = 0
for valor in lista_1:
    vezes = lista_1.count(valor)
    if vezes > cont:
        cont = vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra} e apareceu {cont}x')

for tipo in lista_2:
    print(tipo.strip().capitalize())

print()

frase = 'O Brasil vai ser hexa em 2022.'
lista = frase.split(' ')
lista_01 = '='.join(lista)

print(lista)
print()
print(lista_01)

print()

n = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

for v in n:
    print(v)
    print()

for b in n:
    print(b[0], b[1])


print()

nome_cad = [
    ['Joao', 30],
    ['Maria', 22],
    ['Pedro', 18],
    ['Ana', 8]
]

for indice, nom in nome_cad:
    print(indice, nom)

print()
nomes = ['Bruno', 'Renata', 'Rafaela', 'João', 'Maria']
n1, n2, n3, n4, n5 = nomes

print(n2)
print(n5)
print(n1)

