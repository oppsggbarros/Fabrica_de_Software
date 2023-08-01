from Retangulo import *
while True:

    print("Escolha um desses para fazer a ação\n1-Calcular area\n2-Calcular perímetro\n3-Mudar os valores\n0-Sair")
    a = input()
    if a == "1":
        ladoA = int(input("Digite o comprimento do retângulo: "))
        ladoB = int(input("Digite a altura do retângulo: "))
        area = Retangulo(ladoA, ladoB)
        area.calcular_area()