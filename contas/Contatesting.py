from Conta import *

while True:
    print("Digite o número indico para fazer a ação")
    a = int(input("1- Cadastro\n2- Depósito\n3- Saque\n4- Extrato\n 0- Sair"))
    if a == 1:
        agencia = input("Digite o número da agência: ")
        conta = input("Digite o número da conta: ")
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        saldo = int(input("Digite seu saldo:"))
        fone = input("Digite seu telefone: ")
        c = Conta(agencia, conta, nome, cpf, saldo, fone)
        c.cadastro(agencia, conta, nome, cpf, saldo, fone)
        print(c.agencia, c.conta, c.nome, c.fone, c.cpf)
    if a == 2:
        depositara = int(input("Digite o valor para depositar:"))
        c = Conta(depositara)
        c.depositar(depositara)

