a=0
cont = 1
for i in range(50):
    preço = a + 1.99
    a = preço
    print(cont, "- R$ %.2f"%preço)
    cont=cont+1