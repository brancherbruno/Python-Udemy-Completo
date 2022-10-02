# aula 23 é sobre comandos de input. Vou realizar uns exp pois já entendo sobre

n = str(input("Digite seu nome: "))
ano = int(input(f"{n} digite o ano em que você nasceu [0000]: "))
ps = float(input(f"{n} digite seu peso [00.00]: "))
alt = float(input(f"{n} digite sua altura [00.00]: "))

imc = ps/alt**2
idd = 2022 - ano

print(f"{n} você nasceu em {ano} e tem {idd} anos. Seu peso é de {ps}kg e sua altura é {alt}m. Seu IMC é {imc:.02f}.")
