"""
Criar variáveis para NOME(str), IDADE(int), ALTURA(float), PESO(float)
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa com base na idade dela (int)
Obter o IMC da pessoa com base no peso e altura dela (float)
Exibir os valores em F-strings
"""

n = "Bruno de Souza Brancher"
idd = int("36")
alt = float("1.80")
pes = float("90.85")
ano = int("2022")
nasc = int(ano - idd)
imc = pes/alt**2

print(f'{n} nasceu em {nasc}, tem {idd} anos de idade. Mede {alt:.2f}m de altura e pesa {pes} kg. Seu IMC é {imc:.2f}.')



