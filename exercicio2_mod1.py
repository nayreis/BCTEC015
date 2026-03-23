while True:

    primeiro = input("Digite o primeiro número: ")
    segundo = input("Digite o segundo número: ")

    try:
        primeiro = float(primeiro)
        segundo = float(segundo)
        
    except ValueError:
        print("Erro: digite apenas números válidos.\n")
        continue

    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite a opção: ")

    if operacao == "1":
        resultado = primeiro + segundo
    elif operacao == "2":
        resultado = primeiro - segundo
    elif operacao == "3":
        resultado = primeiro * segundo
    elif operacao == "4":
        if segundo == 0:
            print("Erro: divisão por zero.\n")
            continue
        resultado = primeiro / segundo
    else:
        print("Operação inválida.\n")
        continue

    print("Resultado:", resultado)

    continuar = input("\nDigite ENTER para continuar ou F para finalizar: ").upper()

    if continuar == "F":
        print("Programa finalizado.")
        break
