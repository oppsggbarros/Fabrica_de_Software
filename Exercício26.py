par=[]
impar = []
for i in range(10):
    num = int(input("Digite um número: "))
    if num%2 ==0:
        par.append(num)
    else:
        impar.append(num)
print("Há", len(par), "números pares")
print(par)
print("Há", len(impar), "números impares")
print(impar)