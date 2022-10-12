"""
Revisão while
"""

d = 0
while d <= 10:
    print(d)
    d = d + 1
print('Terminou')
print()
print()
print('='*20)
"""
No comando while podemos inserir o comando continue, isso faz com que o python pule os processos e continue a realizar 
o laço sem interrupção.
"""
print()
a = 0
while a <= 10:
    if a == 4:
        a = a + 1
    print(a)
    a = a + 1
print('Acabou')

print()
print('='*20)
print()
print()


b = 0
while b <= 10:
    if b == 5:
        b = b + 1
        break
    b = b + 1
    print(b)
print('Acabou')


print()
print('='*20)
print()
print()


x = 0

while x < 10:
    y = 0
    while y < 5:
        print(f'X tem o valor de {x} e Y tem o valor de {y}')
        y += 1
    x += 1
print('Acabou')



print()
print('='*20)
print()
print()

while True:
    n1 = input('Digite um valor: ')
    n2 = input('Digite um segundo valor: ')
    ope = input('Digite um operador [+ - * /]: ')
    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número, por favor refaça a operação.')
        continue
    n1 = int(n1)
    n2 = int(n2)
    if ope == '+':
        som = n1 + n2
        print(f"A soma dos valores de {n1} e {n2} é: {som}")
    elif ope == '-':
        sub = n1 - n2
        print(f"A subtração de {n1} por {n2} é:  {sub}")
    elif ope == '*':
        mult = n1 * n2
        print(f"A multiplicação de {n1} por {n2} é:  {mult}")
    elif ope == '/':
        div = n1 / n2
        print(f"A divisão de {n1} por {n2} é: {div}")
    else:
        print('Por favor digite um operador válido: ')
    s = input('Deseja sair? [S/N]: ')
    if s == 'S' or 's':
        break
    else:
        pass

print('Acabou')


