vendas = [192,111,111,1232,77,88,9,33,333,127,100,77,7812,1121,33,232,999,10000,]
meta = 100
qtde_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
       qtde_bateu_meta +=1
qtde_funcionarios = len(vendas)
print('O percentual de pessoaque bateram a meta foi de {:.1%}'.format (qtde_bateu_meta / qtde_funcionarios))