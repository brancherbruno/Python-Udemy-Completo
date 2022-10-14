"""
For in
Função range(start=0, stop, step=1)
"""

frase = 'A maioria dos problemas no TI, é problema de BIOS.'
nf = ''
for letra in frase:
    if letra == 'o':
        nf += letra.upper()
    else:
        nf += letra
print(nf)

print()
print()
print('='*40)
print()
print()

for n in range(1, 10, 2):
    print(n)

print()
print()
print('='*40)
print()
print()

a = 'arara'
b = ''

for c in a:
    if c == 'a':
        b = b + c.upper()
    else:
        b += c
print(b)

print()
print()
print('='*40)
print()
print()


nome = 'Bruno de Souza Brancher'
o = ''

for letra in nome:
    if letra == 'o':
        #continue
        o = o + letra.upper()
        #break
    elif letra == 'n':
        continue
        o = o + letra.upper()
        #break
    else:
        o += letra
print(o)



