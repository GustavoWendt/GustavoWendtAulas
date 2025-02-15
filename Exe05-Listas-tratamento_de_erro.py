produtos=['tv','celular','mouse','teclado',"tablet","geladeira","forno"]
item_usuario= input("Qual item deseja remover? ")
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print('O produto {} não existe na lista.'.format(item_usuario))


produtos=['tv','celular','mouse','teclado',"tablet","geladeira","forno"]
item_usuario= input("Qual item deseja adicionar? ")
produtos.append(item_usuario)
print(produtos)
