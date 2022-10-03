"""
Operadores relacionais:

== igual a
=> maior ou igual
=< menor ou igual
> maior
< menor
!= diferente

todos esses operadores vão retornar um valor booleano

"""
print('=-'*45)
print("Calculador de idade mínima e máxima pra jogar em um \ncampeonato em que o atleta tenha que ter entre 16 e 20 anos")
print('=-'*45)
print()
n = str(input("Digite o nome do jogador: "))
idd = int(input(f"Digite a idade de {n}: "))
print()
print('=-'*45)

if idd >= 16 and idd <= 20:
    print(f"{n} pode ser inscrito está apto a participar do campeonato.")
else:
    print(f"{n} não poderá ser inscrito pois a idade não atende os parâmetros solicitados.")


