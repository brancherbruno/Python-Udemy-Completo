"""
Variáveis:
adotar padrão para serem sempre em letras minúsculas, se forem nomes compostos colocar separador _
PS: valor booleano explícito a primeira letra precisa ser maiúscula
"""

nome = 'Bruno'
idade = 36
altura = 1.80
data_nascimento = 1986
maior_idade = True
peso = 90

print(nome, 'tem', idade, 'anos,', 'nasceu em', data_nascimento, 'tem', altura, 'm', 'e é maior de idade?', maior_idade)
print('O IMC de', nome, 'é', peso//altura**2)
