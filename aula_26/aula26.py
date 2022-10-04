"""
Operadores lógicos em Python:

and - E, por ex: 5 é maior que 10 E menor que 4?
or - OU, por ex: 5 é maior que 10 OU menor que 4?
not - NÃO, por ex:
in
not in


AND
(verdadeira E verdadeira) = verdade - só vai retornar verdade se as 2 variáveis forem verdadeira.
(verdadeira E falsa) = falso
 variavel1 and variavel2


OR
Na comparação com OR, se uma das 2 variáveis for verdadeira, vai retornar verdadeiro. Para retornar falso as 2 variáveis
precisam ser falsas.

variavel1 or variavel2


NOT
Conhecido também como inversor, precisa somente de uma variável para comparação, ou seja, pede que a variável não
seja aquela citada.

Ex:
"""
a = 6
b = 9

if not b > a:  # nessa expressão a palavra not vai fazer com que seja invertido o valor e a segunda sentença seja impressa
    print('B é maior que A')
else:
    print('A é maior que B')

"""
Posso usar também com uma variável vazia:
"""
a = ''
b = 0

if not a:
    print('Por favor insira o valor de A')

""""
Nesse caso a sentença é: se A não tem valor nenhum imprime xxxxx, se tiver algo escrito nada será mostrado na tela.

Mesma coisa do valor de B, mas nesse caso, se for zero, vai retornar o print pois o 0 é considerado um valor booleano
falso.

"""

"""
IN e NOT IN

É a condição de ter ou não algo dentro da variável

"""

# exemplo simples de um código para login

nome = str(input('Digite seu nome: '))
senha = input('Digite sua senha: ')

user_db = 'bruno'
senha_db = '12345'

if user_db == nome and senha_db == senha:
    print('Usuário logado com sucesso!')
else:
    print('Usuário ou senha inválidos. Tente novamente.')





