"""
Listas
Fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
#  +     0    1    2    3    4    5
lista = ['a', 'b', 'c', 'd', 'e', 'f']
#   -    -6   -5   -4   -3   -2   -1

print(lista[0::2])
print()
print('=' * 20)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print(l1)
print(l2)
print(l1 + l2)
print()
print('=' * 20)
l1.extend(l2)  # comando para adicionar algo a mais na lista selecionada

print(l1)
print(l2)

print()
print('=' * 20)

l3 = [1, 2, 3, 4, 5]
l4 = [6, 7, 8, 9, 10]

l4.append('B')  # insere um valor no último lugar da lista

print(l3)
print(l4)

print()
print('=' * 20)

l3.insert(3, 'Bruno')  # para inserir um valor em qualquer lugar da lista. Basta informar em qual índice da lista você
# quer o item e qual item você quer por na lista.

print(l3)

"""
para excluir um item da lista, usar o pop
"""
print()
print('=' * 20)

l3.pop(3)
l4.pop(-1)  # posso deixar em branco para eliminar o último item da lista também.

print(l3)
print(l4)

print()
print('=' * 20)

"""
para deletar uma parte da lista utilizar del.
"""

del (l4[1:4:])

print(l3)
print(l4)

print()
print('=' * 20)

l4.insert(1, 7)
l4.insert(2, 8)
l4.insert(3, 9)
tot = l3 + l4
print(tot)
print(max(tot))

print(min(tot))

print()
print('=' * 20)

"""
para listar mais rapidamente, utilizar o range, porém precisa iterar com list, conforme exemplo abaixo.
"""
l5 = list(range(1, 11))
print(l5)

print()
print('=' * 20)

l6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for item in l6:
    soma = soma + item
print(soma)

print()
print('=' * 20)

"""
exemplo de jogo de adivinhação
"""

secreto = "PROGRAMADOR"
let_user = []
chance = 3

nome = str(input('Qual seu nome: ')).title()
while True:
    '''linha 118 a 130: comando caso o usuário erre 3x a letra e solicita se o usuário quer continuar a jogar, caso
     a resposta seja positiva, vai limpar a variável SEC_TEMP, a lista LET_USER e reiniciar as chances para 3, caso
     negativo vai agradecer e finalizar o executável'''
    if chance == 0:
        print(f'Que pena {nome}, você perdeu!')
        des = input(f'{nome} deseja jogar novamente? [S/N]: ').upper()
        if des == 'S':
            sec_temp = ''
            let_user.clear()
            chance = chance + 3
            continue
        else:
            print(f'Obrigado por jogar, {nome}.')
            break
    letra = str(input(f'{nome} digite uma letra: ')).upper()

    '''linha 135 a 138: comando para informar que o usuário deve digitar somente uma letra. Comando também soma uma 
    letra a lista de letras do usuário (caso ele digite uma letra somente)'''
    if len(letra) > 1:
        print(f'Isso não vale {nome}, digite apenas uma letra! Tente novamente!')
        continue
    let_user.append(letra)

    '''linha 143 a 147: comando para informar que a letra está ou não na palavra secreta. Caso a letra não seja a 
    correta o sistema vai zerar apagar a última letra digitada incorretamente.'''
    if letra in secreto:
        print(f'A letra "{letra}" está na palavra secreta {nome}!')
    else:
        print(f'Que pena! A letra "{letra}" não está na palavra secreta. {nome}, tente novamente!')
        let_user.pop()

    '''linha 153 a 159: cria uma variável temporária SEC_TEMP para as letras que o usuário digitar corretamente e mostra
    em tela as letras corretas e as letras a adivinhar. O código vai verificar se a varável temporária ADV está   
    contida na variável SECRETO. Se estiver contido na variável SECRETO, o código vai verificar se a variável ADV 
    está contido na lista LET_USER e vai somar a variável ADV dentro da variável SEC_TEMP junto com as letras já 
    contidas nela e agregar um * as letras não adivinhadas.'''
    sec_temp = ''
    for adv in secreto:
        if adv in let_user:
            sec_temp += adv
        else:
            sec_temp += '*'
    print(sec_temp)

    '''linha 169 a 177: verifica se as letras da variável temporária SEC_TEMP é igual a palavra da variável SECRETO.
    Se for igual, vai informar o usuário que ele adivinhou a palavra e solicitar se quer jogar novamente. Caso o 
    usuário informar que sim, ele vai limpar a variável SEC_TEMP e limpar a lista LET_USER para recomeçar o jogo.'''
    if sec_temp == secreto:
        print(f'Parabéns {nome}, você adivinhou a palavra secreta: {secreto}!')
        des = input(f'{nome} deseja jogar novamente? [S/N]: ').upper()
        if des == 'N':
            print(f'Obrigado por jogar {nome}')
            break
        else:
            sec_temp = ''
            let_user.clear()
    '''linha 174 a linha 176: no começo do código é criado a chance de 3 tentativas do usuário acertar a palavra. Caso 
    o usuário não acerte o código abaixo vai diminuindo as chances do usuário até zerar, mostrando sempre quantas
    chances o usuário tem.'''
    if letra not in secreto:
        chance -= 1
    print(f'Você ainda tem {chance} chance(s) {nome}.')
    print()
print('=' * 20)
