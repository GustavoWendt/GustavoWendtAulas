#vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720,'Iphone':1200}
#vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920,'Iphone':1210000}
#del vendas_tecnologia2['iphone']
#print(vendas_tecnologia2)
#Para testar tire os como comentario

#vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720}
#vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920}
#vendas_tecnologia_excluido=vendas_tecnologia2.pop('Samsug galaxy')
#print(vendas_tecnologia2)
#print(vendas_tecnologia_excluido)
#vendas_tecnologia2.clear()
#print(vendas_tecnologia2)


vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720}
vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920}
for chave in vendas_tecnologia2:
    print(chave)


    vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720}
vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920}
for chaves in vendas_tecnologia2:
    print("O produto {} vendeu {} undades.".format(chave, vendas_tecnologia2[chaves]))



    vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720}
vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920}
for item in vendas_tecnologia2.items():
    print(item)




    vendas_tecnologia = {'iphone':1500,'Samsug galaxy':1200,'Tv Samsung':10000,'ps5':14300,'tablet':1720}
vendas_tecnologia2 = {'iphone':15000,'Samsug galaxy':100200,'Tv Samsung':100900,'ps5':14307890,'tablet':1799920}
for produto, vendas in vendas_tecnologia2.items():
   print('{}: {} de unidades.'.format(produto,vendas))