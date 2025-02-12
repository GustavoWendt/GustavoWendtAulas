#Faça um programa que o usuario digite um número e diga se o número é superior a 20 inferior a 10 ou se está entre 10 e 20.
num=float(input("Digite um número: "))
if num >20:
  print("Número maior que 20")
elif num <10:
  print("Número menor que 10")
else:
  print("Número entre 10 e 20")