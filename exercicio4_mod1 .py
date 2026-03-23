
while True:

    cnpj = input("Digite os 12 primeiros dígitos do CNPJ: ")

    soma = 0
    num = 2

    inverso = cnpj[::-1]

    for i in inverso:
        soma = soma + int(i) * num
        num = num + 1

        if num > 9:
            num = 2

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto


    cnpj2 = cnpj + str(digito1)

    soma = 0
    num = 2

    inverso = cnpj2[::-1]

    for i in inverso:
        soma = soma + int(i) * num
        num = num + 1

        if num > 9:
            num = 2

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto


    print("Dígitos verificadores:", digito1, digito2)

    sair = input("Digite F para finalizar: ")

    if sair == "f":
        break
