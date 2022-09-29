# Tipos de dados primitivos, str, int, float, bool
# BOOL - só aceita true/false ou seja é de lógica ou comparação
print("Bruno", type("Bruno"))
print(36, type(36))
print(10.4, type(10.4))
print(5 == 5, type(5 == 5))
print(-15.23, type(-15.23))
print(-8, type(-8))
print("B" == "B", type("B" == "B"))
print("B" == "b", type("B" == "b"))
print('='*20)
# algumas coisas em python são avaliadas como falsas, por exemplo, se eu informar uma str vazia, vai avaliar como falso.
# bem como o número zero também é avaliado como falso
print(bool(''))
print(bool(0))
print('='*20)
# qualquer valor que não seja vazio dentro de uma str que seja convertida para bool, será true. Se for valor vazio
# será avaliado como falso
print('Bruno', type('Bruno'))
print('Bruno', type('Bruno'), bool('Bruno'))
print('='*20)
# Typer casting: converter um tipo de dado primitivo em outro
print('10', type('10'), type(int('10')))
print('='*20)

# exercício
# verificação de nome - str
print('Bruno', type('Bruno'))
# verificação de idade - int
print('35', type(int('35')))
# verificação de altura - float
print('1.80', type(float('1.80')))
# verificação de maioridade - bool
print('35', type(int('35')), bool(int('35' >= '18')))


