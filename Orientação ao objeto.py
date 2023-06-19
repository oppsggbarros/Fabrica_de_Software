def hello(nome, idade):
    print("Olá!",  nome, "Sua idade é", idade)
nome = input("Nome: ")
idade = int(input("Sua idade: "))
hello (nome, idade)
def calcular_pagamento(qtd_horas,valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    print(salario)
calcular_pagamento(80,2)
def soma(x,y):
    result=x+y
    print(result)
    return result
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
res = soma(a,b)
print("Soma: ", res)
def inverte(nome, sobrenome):
    nomeInverso = sobrenome+','+nome
    return nomeInverso
nome =input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido = inverte(nome, sobrenome)
print("Olá", invertido)
def par(x):
    if(x%2)==0:
        return True
    else:
        return False
while True:
    num = int(input("Insira um número: "))
    if par(num):
        print("É par")
    else:
        print("É Ímpar")
def cadastro():
    name = input("Qual seu nome: ")
    age = int(input("Idade: "))
    return name, age
print("Iniciando Cadastro...")
nome, idade =cadastro()
print("Seu nome é",nome, "Sua idade é", idade)