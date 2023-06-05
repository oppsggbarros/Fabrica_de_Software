import os
while True:
    print("Digite o número para ir para a ação")
    a =input("1- Cadastrar\n2- Cadastro do Avião\n3- Cadastro de Passagem\n4- Cadastro da Tripulação\n5- Imprimir Relatórios\n0- Encerrar\n")
    os.system("cls")
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
        modelo = input("Informe o modelo do avião: ")
        while True:
            try:
                ano = int(input("Informe o ano do Avião: "))
                qntd = int(input("Informe a quantidade de Passageiros: "))
            except ValueError:
                print("Coloque somente número!")
                continue
            else:
                break
        horario = input("Informe as horas de voo: ")
        cor = input("Qual a cor do Avião: ")
        os.system("pause")
        os.system("cls")
    elif a =="3":
        destino = input("Informe o Destino da viagem: ")
        origem = input("Informe a Origem da viagem: ")
        duração = input("Qual é o tempo total da viagem: ")
        while True:
            try:
                valor = float(input("Qual o valor da passagem: "))
            except ValueError:
                print("Infome somente o preço!")
                continue
            else:
                break
        os.system("pause")
        os.system("cls")
    elif a == "4":
        nometrip = input("Nome da tripulação: ")
        cargo = input("O cargo da pessoa: ")
        while True:
            try:
                idadetrip = int(input("Idade da tripulação:"))
                fonetrip = int(input("Telefone da tripulação"))
            except ValueError:
                print("Informe somente números: ")
                continue
            else:
                break
        os.system("pause")
        os.system("cls")
    elif a == "5":
        try:
            print(name)
            print(sobrenome)
            print(rg)
            print(cpf)
            print(endereço)
            print(fone)
            print(idade)
            print(destino)
            print(origem)
            print(duração)
            print(valor)
            print(modelo)
            print(ano)
            print(horario)
            print(cor)
            print(qntd)
            print(nometrip)
            print(idadetrip)
            print(fonetrip)
        except NameError:
            print("Faça o cadastros primeiro!")
        os.system("pause")
        os.system("cls")
    elif a == "0":
        break