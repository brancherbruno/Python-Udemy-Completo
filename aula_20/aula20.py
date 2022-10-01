
nome = 'Bruno'
idade = 36
altura = 1.80
data_nascimento = 1986
maior_idade = True
peso = 90
imc = peso/altura**2
print(nome, 'tem', idade, 'anos,', 'nasceu em', data_nascimento, 'tem', altura, 'm', 'e é maior de idade?', maior_idade)
print('O IMC de', nome, 'é', peso//altura**2)
"""
Para formatar uma informação em tela, basta usar a letra F antes das aspas, e para inserir as variáveis, basta colocar
dentro de chaves, conforme no exemplo abaixo. E para arredondar os valores que por ventura venham com muitas casas decimais
basta formatar da seguinte maneira: {variável:.quantidade de casas decimais desejada após a vírgulaf}
Pode ser usado também o .format no final. Dentro dos colchetes se eu colocar a numeração de ordem posso dizer onde cada
informação (variável) será inserida - lembrando que sempre começa por 0.
"""
print(f'{nome} tem {idade} anos de idade, nascido em {data_nascimento}, tem {altura} e pes {peso}kg. Seu IMC é de {imc}.')
print(f'{nome} tem {idade} anos de idade, nascido em {data_nascimento}, tem {altura} e pes {peso}kg. Seu IMC é de {imc:.2f}.')
print("{} tem {} anos de idade.Seu IMC é de {:.2f}.".format(nome, idade, imc))
