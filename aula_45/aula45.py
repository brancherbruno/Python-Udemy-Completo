"""
Operador Ternário
"""

log_user = True  # para mostrar logado, basta colocar como TRUE
'''
if log_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário não logado.'

print(msg)

'''
'''
msg = 'Usuário logado.' if log_user else 'Usuário precisa logar.'
print(msg)
'''

idd = input('Qual sua idade? ')
if not idd.isnumeric():
    print('Você deve digitar somente números. Tente novamente.')
else:
    idd = int(idd)
    maior = (idd >= 18)
    msg = 'Pode logar.' if maior else 'Você é menor de idade.'

    print(msg)

