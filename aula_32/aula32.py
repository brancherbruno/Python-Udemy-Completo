"""
Formatando valores com modificadores

:s - textos (str)
:d - inteiros (int)
:f - números de ponto flutuantes (float)
:. - (número)f - quantidade de casas após a vírgula (float)
: - (caractere) (> ou < ou ^) (quantidade) (tipo -s, d ou f)

> - esquerda
< - direita
^ - centro
"""

n1 = 10
n2 = 3

tot = n1/n2

print('{:.2f}'.format(tot))
print(f'{tot:.2f}')
"""
para delimitar que minha variável vai ter um total de x casas, utilizo a regra abaixo. Nesse caso, estou informando que
minha variável terá 10 casas decimais e os restante será preenchido por números zeros à esquerda.
"""

n3 = 5

print(f'{n3:0>10}')

n4 = 1986

print(f'{n4:0>10}')

n5 = 36

print(f'{n5:0^10}')


nome = 'Bruno de Souza Brancher'
print(len(nome))

print((50-len(nome))/2)

print(f'{nome:#^50}')

nome_f = '{:@>25}'.format(nome)
print(nome_f)

nome_f1 = '{n}{n}{n}'.format(n=nome)
print(nome_f1)

nome_f2 = 'Bruno'
sobre1 = 'de Souza'
sobre2 = 'Brancher'

nomefo = '{2:#^20} {0:=^20}'.format(nome_f2, sobre1, sobre2)

print(nomefo)

nome = nome.ljust(40, "#")
print(nome)

nomecomp = 'Bruno de Souza Brancher'
nome01 = nomecomp.rjust(40, '#')
print(nome01)

nono = 'Bruno de Souza Brancher'

print(nono.lower())
print(nono.upper())
print(nono.title())



