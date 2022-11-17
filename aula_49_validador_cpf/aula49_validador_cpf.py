nome = input(str('Olá, digite seu nome por favor: ')).title()

while True:
    cpf_user = input(f'{nome} digite seu CPF sem pontos nem traço: ')

    # para separar os 9 primeiros digitos do cpf
    cpf = cpf_user[:-2]
    'contador do valor reverso e calculo'
    r = 10
    total = 0

    # calculo em um loop - no total são 19 calculos + calculos separados
    for v in range(19):
        if v > 8:
            v -= 9
        total += int(cpf[v]) * r
     # para calcular o valor final
        r -= 1
        if r < 2:
            r = 11
            n = 11 - (total % 11)
            if n > 9:
                n = 0
            total = 0
            cpf += str(n)

    if cpf == cpf_user:
        print('Válido')
    else:
        print('Inválido')
