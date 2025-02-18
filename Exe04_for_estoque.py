estoque = [1000,984938,33,444,3434,2,13,233,23232,84748]
produtos=['coca-cola','pepsi','guarana','sprit','fanta','Agua da serra','Brahma','Dolly','Wiski']
nivel_minimo = 50
for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(produtos [i],qtde)