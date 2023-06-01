b = int(input("Quantos pães você quer: "))
a=0
cont = 1
for i in range(b):
    preço = a + 0.18
    a = preço
    print(cont, "- R$ %.2f"%preço)
    cont=cont+1