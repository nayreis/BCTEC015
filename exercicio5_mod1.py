#Faça um programa em Python utilizando os comandos (entrada e saída de dados, estruturas condicional 
# e de repetição), que imprima na tela um MENU contendo as opções:
#1=Incluir usuário
#2=Excluir usuário
#3=Consultar usuário
#4=Alterar usuário
#5=Listar todos os usuários que estão cadastrados
#9=Sair.
#Funcionalidades necessárias:
#a) o programa só deve ser finalizado quando o usuário digitar a opção 9=Sair;
#b) caso o usuário digitar as demais opções, deverá ser impresso o número e nome da opção e em seguida finalizar o programa
#c) caso o usuário digite alguma opção não prevista, deverá ser impresso uma mensagem de 
# opção inválida e o programa não poderá ser finalizado.

while True: 
    print("  MENU \n\n 1= Incluir Usuário \n 2= Excluir Usuário \n 3=Consultar Usuário \n 4=Editar Usuário \n 5= Listar todos os Usuários que estão cadastrado \n 9= Sair\n")
    
    menu= input("Digite uma opção: ")
    if menu== "9":
        print ( "\nSaindo do Sistema.\n ")
        break
    elif menu== "1":
        print("\n Opção 1 - Incluir Usuário \n")
        print ( "Saindo do Sistema. ")
        break
    elif menu== "2":
        print("\n Opção 2 - Excluir Usuário \n ")
        print ( "Saindo do Sistema. ")
        break
    elif menu== "3":
        print("\n Opção 3 - Consultar Usuário \n")
        print ( "Saindo do Sistema. ")
        break
    elif menu== "4":
        print("\n Opção 4 - Editar Usuário \n")
        print ( "Saindo do Sistema. ")
        break
    elif menu== "5":
        print("\n Opção 5 - Listar todos os Usuários \n")
        print ( "Saindo do Sistema. ")
        break
    else:
        print("\n Opção inválida\n")
        
    