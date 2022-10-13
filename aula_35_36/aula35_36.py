"""
Laços de repetição while/else
"""
#
# contador = 1
# acumulador = 1
#
# while contador < 10:
#     print(f'Contador: {contador}')
#     print(f'Acumulador: {acumulador}')
#     acumulador = acumulador + contador
#     contador += 1
# else:
#     print(f'O valor contato no final é {contador} e foi acumulado o total de {acumulador}')

print()
print()
print('='*40)

"""
Iterando strings com while

Índices:
01234567.....
"""
print()
print()

frase = 'O maior problema em informatica não é o hardware ou o software, quase sempre está localizado entre a cadeira e o monitor'
tam = len(frase)
nova_f = ''
contador = 0
#
# while contador < 31:
#     print(frase[contador], contador)
#     contador += 1

desc = input('Qual letra você quer deixar maiúscula? ')

while contador < tam:
    letra = frase[contador]
    if letra == desc:
        nova_f += desc.upper()
    else:
        nova_f += letra
    contador += 1
print(nova_f)
print(f'A frase tem {tam} letras')



