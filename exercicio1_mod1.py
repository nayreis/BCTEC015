#Faça um programa em Python que receba o valor de uma conta e um percentual de 
#desconto. Calcule o novo valor da conta ao 
#ser aplicado o percentual de desconto e escreva o resultado obtido

conta=float(input("Digite o valor da conta: "))
desconto=float(input("Digite o percentual de desconto: "))

novo_valor= conta-((conta*desconto)/100)

print("Valor com desconto é: R$",novo_valor)