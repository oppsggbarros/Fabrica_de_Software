import os
while True:
    print("Digite o número para ir para a ação")
    a =input("1- Cadastrar\n2- Cadastro da Passagem\n3-Cadastro do Avioã 5- Imprimir Relatórios\n0- Encerrar\n")
    if a =="1":
        name = input("Informe seu nome: ")
        sobrenome = input("Informe seu sobrenome:")
        while True:
            try:
                rg = int(input("Informe seu RG: "))
                cpf = input("Informe seu CPF: ")
                fone = int(input("Informe seu Telefone: "))
                idade = int(input("Informe sua Idade: "))
            except ValueError:
                print("Digite somente números")
                continue
            else:
                break
        endereço = input("Informe seu Endereço: ")

        os.system("pause")
        os.system("cls")
    elif a == "2":
        print("Nome do passageiro:", name)
        print("Sobrenome do passageiro:", sobrenome)
        print("RG do passageiro")