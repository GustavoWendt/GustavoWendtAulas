#Transforme apenas a primeira letra de uma string em maiuscula.
nome = "gustavo"
print(nome.capitalize() ,"\n")


#Transforme todas as letras em minuscula
nome = "GUSTAVO"
print(nome.casefold() ,"\n")


#CONTA O NÚMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.
nome= "gustavowendt14@gmail.com"
print(nome.count ('a'),"\n")


#RETORNA TRUE (VERDADEIRO) OU FALSE (FALSO) PARA UM TESTE SE A STRING TERMINA COM UMA STRING ESPECIFICA.
nome = "gustavowendt14@gmail.com"
print(nome.endswith ('gmail.com'), "\n")

#ENCONTRA A POSIÇÃO DO TERMO PROCURADO.   LEMBRE-SE COMEÇA DO ZERO.
nome = "gustavowendt14@gmail.com"
print(nome.find('@'), "\n")


#VERIFICA SE O TEXTO É TODO FEITO COM LETRAS.
nome = "Gustavo"
print(nome.isalpha(),"\n")


#VERIFICA SE O TEXTO É FEITO COM NÚMEROS.
nome = "123"
print(nome.isnumeric(),"\n")


#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO.
Nome = "Gustavo"
print(nome.replace('g','u'),"\n")


#SEPARE O TEXTO STRING Baseado em algum caractere indicado.
nome = "gustavowendt14 @ gmail.com"
print(nome.split ('@'),"\n")


#COLOCAR TODAS AS LETRAS INICIAIS EM MAIUSCULA.
nome="gustavo wendt"
print(nome.title(),"\n")


#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO ESPAÇOS QUE NÃO AGREGAM VALOR.
nome="Gustavo Wendt"
print(nome.strip(),"\n")


#RETORNA TRUE OU FALSE PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO.
nome="gustavo 2008"
print(nome.startswith ("ser"),"\n")
print(nome.startswith ("Ser"),"\n")


