#Faça um programa que receba uma nota do aluno e se for superior ou igual a 7(sete) apareçamensagem que ele está aprovado, se for inferior a 5 (cinco) ele está "não aprovado/reprovou direito" e se estiver entre 5 (cinco) e 7 (sete apareça mensagem "Não aprovado/Recuperação.
nota=float(input("Digite sua nota: "))
if nota >=7:
    print("O aluno está aprovado")
else:
  if nota<=5:
    print("O aluno não está aprovado/reprovado")
  else:
    print("O aluno está em recuperação")
