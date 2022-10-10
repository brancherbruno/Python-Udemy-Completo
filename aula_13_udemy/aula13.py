print('Bruno', 'de', 'Souza', 'Brancher', sep="-")
# o python por padrão já deixa informações separadas se elas forem colocadas separadas por vírgulas, porém
# para selecionar um separador de caracteres diferente, basta utilizar o comando sep= e colocar entre aspas duplas o
# marcador que você deseja.
print('Renata', 'Bom', 'Morgan', sep="*")
# agora para deixar todos os textos na mesma linha, basta colocar end=""
print("Teste", "de", "texto", "na", "mesma", "linha", sep="-", end="")
print("outra", "linha", "com", "texto", sep="-")
# no caso acima, o end="" deixou tudo na mesma linha (rodar o comando para verificar)
# se for colocado um separador dentro do end="" ele vai juntar as frases e separar as frases pelo separador escolhido
print("Teste", "de", "texto", "na", "mesma", "linha", sep="-", end="***")
print("outra", "linha", "com", "texto", sep="-")

cpf = input("Digite um CPF sem os separadores: ")
print("O CPF digitado é: {}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11]))
# a formatação acima só vale para input normal. Verificar mais tarde para input de int e float

print("062", "007", "389", sep=".", end="-")
print("63")

