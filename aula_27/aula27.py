"""
user = input('Digite o nome do usuário: ')

carac = len(user)  # retornando o type de carac, o len sempre vai ser int

print(user, carac, type(carac))

"""

"""user = input('Digite o usuário: ')

car = len(user)

if car < 5:
    print('Usuário precisa ter mais de 6 letras. Tente novamente!')
else:
    print('Usuário cadastrado com sucesso!')

"""

nome = input('Digite seu nome: ')

sobre = input('Digite seu sobrenome: ')

# cara = len(nome+sobre)

# print(nome, sobre, cara)

print(f'O total de caracteres é {len(nome) + len(sobre)}')

# A função len é somente para STR
