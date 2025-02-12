
while True:  # Começa o loop para repetir o programa
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1 - Subtração")
    print("2 - Divisão")
    print("3 - Soma")
    print("4 - Multiplicação")

    operacao = int(input("Digite o número da operação desejada: "))

    if operacao == 1:
        print("Resultado:", num1 - num2)
    elif operacao == 2:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero não é permitida!")
    elif operacao == 3:
        print("Resultado:", num1 + num2)
    elif operacao == 4:
        print("Resultado:", num1 * num2)
    else:
        print("Opção inválida! Escolha um número entre 1 e 4.")

    # Pergunta se o usuário quer repetir
    loop = input("\nDeseja fazer mais uma operação? (S/N): ").strip().upper()

    if loop != "S":  # Se a resposta for diferente de "S", sai do loop
        print("Encerrando o sistema... O dev é lindo! 😎")
        break  # Sai do loop e encerra o programa