nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))
media = (nota1+nota2)/2
if media >= 7:
    print("Aprovado", end="")
    if media == 10:
        print(" com Distinção")
elif media < 7:
    print("Reprovado")
print("A média foi %.1f"%media)