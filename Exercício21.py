#Exercício 1
lista = []
lista2 = []
for i in range(10):
    lista.append(input("Digite O Nome: "))
for item in lista:
    print(item)
#Exercício 2
for i in range(10):
    lista.append(int(input("Digite um número: ")))
print(sum(lista))
#Exercício 3
for i in range(10):
    lista.append(input("Digite o nome do produto: "))
for itens in lista:
    print(itens)
#Execício 4
for j in range(10):
    n = int(input("Digite um número inteiro: "))
    if n > 0:
        
        lista.append(n)
    elif n < 0:
        lista2.append(n)
print("Número positivos: ", len(lista))
for itens in lista:
    print(itens, end=", ")
print("\nNúmero negativos: ", len(lista2))
for itens in lista2:
    print(itens, end=", ")
#Exercício 5
for n in range(50,101,2):
    print(n)
#Exercício 6
for j in range(10):
    lista.append(input("Digite um número inteiro: "))
for item in lista:
    print(item*item)
#Exercício 7
for j in range(10):
    lista.append(input("Digite um número inteiro: "))
print("Maior número: ", max(lista))
print("Menor número: ", min(lista))
#Exercício 8 
