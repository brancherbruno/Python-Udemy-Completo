"""
Fazer um programa para que o usuário digite um número inteiro, informe se este número é par ou ímpar.
Caso o usuário digite um número que não seja inteiro, informe que o número não é inteiro.
"""

n = input("Digite um valor inteiro: ")

if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print('O valor é par')
    else:
        print('O valor é ímpar')
else:
    print('O valor não é inteiro')

print('=='*30)

"""
Pedir a hora ao usuário e, com esse horário, exibir a saudação apropriada. Ex: bom dia - 0-11; boa tarde 12-17;
boa noite 18-23;
"""


h = input("Digite a hora [0-23]: ")

if h.isdigit():
    h = int(h)
    if (h < 0) or (h > 23):
        print('O horário deverá estar entre 0 e 23h')
    else:
        if (h >= 0) and (h <= 11):
            print('Bom dia')
        elif (h >= 12) and (h <= 17):
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('O valor não é um horário válido')


"""
Programa que peça o nome do usuário, caso nome seja menor que 4 letras avise que o nome é curto;
se tiver de 5 a 6 apareça: seu nome é normal;
se tiver mais de 6, seu nome é muito longo;
"""

n = str(input('Digite seu nome: '))
tam = len(n)

if tam < 4:
    print('Seu nome é muito curto')
elif (tam >= 5) and (tam <= 6):
    print('Seu nome tem tamanho justo')
else:
    print('Seu nome é muito longo')



