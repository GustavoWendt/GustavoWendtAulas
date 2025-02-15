Lista1= [1,2,3,4,5]
Lista2= [6,7,8,9,10]
Lista3= [11,12,13,14,15]
todas_listas=[Lista1,Lista2,Lista3]
print(todas_listas)


produtos=['tv','celular','mouse','teclado',"tablet"]
print(produtos[1])


produtos2=['tv','celular','mouse','teclado',"tablet"]
vendas2= [1000,  1500,      350,    270,     900]
print("As vendas de",produtos2[1],"foram de ",vendas2[1])


produtos3=['tv','celular','mouse','teclado',"tablet"]
i=produtos.index('mouse')
print("O valor de i é "+str(i))
print("A posição do produto i é "+str(produtos3[i]))





nomes=['Alberto','Gustavo','Jonas','Manuela','Carlos']
bairro=['panagua','ani_garibaldi','rua','rua1','rua2']
telefone=[998787878,83792739278,9837393838,20892929,209202]
busca1=input('Digite o nome do usuario: ')
if busca1 in nomes:
 i=nomes.index(busca1)
 bairro_clientes= bairro[i]
 telefone_clientes=telefone[i]
 print("O bairro do cliente", busca1," é", bairro_clientes,"E o telefone é",telefone_clientes )
else:
 print("O cliente",busca1," não está cadastrado:")