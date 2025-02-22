def get_nome():
    nome_usuario = input("Entre com o seu nome: ")
    return nome_usuario

def print_Mensagem(nome_usuario):
    print("Olá Jovem Padawan", nome_usuario)

def main():
    nome_usuario=get_nome()
    print_Mensagem(nome_usuario)

main()