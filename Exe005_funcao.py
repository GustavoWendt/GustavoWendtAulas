def get_data():
    nome_usuario = input("Escreva seu nome: ")
    idade_usuario = int(input("Qual a sua idade?: "))
    tupla_data = (nome_usuario, idade_usuario)
    return tupla_data

def mensagem(nome_usuario,idade_usuario):
    if idade_usuario <=10:
        print("Oi!", nome_usuario)
    else:
        print("Olá!", nome_usuario)

def main():
    nome_usuario,idade_usuario = get_data()
    mensagem(nome_usuario,idade_usuario)

main()
    