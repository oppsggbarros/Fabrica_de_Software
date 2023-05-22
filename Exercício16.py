num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o Terceiro valor: "))
print("O Mais Barato dessa lista é ", end="")

if num1<num2 and num1<num3:
    print(num1)
elif num2<num1 and num2<num3:
    print(num2)
elif num3<num1 and num3<num2:
    print(num3)