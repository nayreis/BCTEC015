#1° digito Soma de 1D*10, 2D*9,... --> soma/11 --> 0 ou 1 =0 diferente --> 11-numero
#2° dígito Soma dos 10 numeros *n-1 --> soma/11--> 0 ou 1 =0 diferente --> 11-numero


while True:

    cpf = input("Digite os nove primeiros digitos do CPF: ")
    
    soma = 0
    soma2 = 0
    soma3 = 0
    num = 10
    num2 = 11
    digito1 = 0
    digito2 = 0

    for i in cpf:
        soma = soma + int(i) * num
        num = num - 1
    
    digito1 = (soma * 10) % 11

    if digito1 == 10:
        digito1 = 0


    for i in cpf:
        soma2 = soma2 + int(i) * num2
        num2 = num2 - 1

    soma3 = soma2 + (digito1 * 2)
    
    digito2 = (soma3 * 10) % 11

    if digito2 == 10:
        digito2 = 0


    print("Dígito verificador:", digito1,digito2)

    sair = input("Digite F para finalizar: ")

    if sair == "f":
        break
