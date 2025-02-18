pessoas_presentes = ['John Snow','Jesse Pinkman','Aria Stark','Tyrion Lennister']
chamada = ' Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para ostrar que o for passou por essa pessoa:'+str(pessoa))