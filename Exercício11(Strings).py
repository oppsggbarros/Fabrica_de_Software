name = str(input("Escreva seu nome: "))
print(name.capitalize())
print(name.upper())
print(name[:8])
print(name.count("a"))

number = int(input("Digite um número: "))
print("O número informado foi %d"%number)


number1 = int(input("Escreva um número: "))
number2 = int(input("Escreva um número: "))
total = number1 + number2
print("%d + %d é %d"%(number1, number2, total))

nome = input("digite seu nome: ")
serie = input("Digite sua Série: ")
escola = input("Digite o nome de sua escola: ")
cidade = input("Digite sua cidade Natal: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4
print("Seu nome é %s\nSua série é %s\nSua escola é %s\nSua cidade é %s"% (nome, serie, escola, cidade))
print("Sua média foi de %f"%media)

raio = float(input("Qual o raio do círculo: "))
area = raio**2*3.14159
print(area)

lado = float(input("Digite o lado do quadrado: "))
areia = lado**2
print("A area do quadrado é %.1f\n"%areia, "O dobro dessa área é", (areia*2))

salario = float(input("Quanto você ganha por hora trabalhada: "))
hora = float(input("Quantas horas você trabalhou esse mês: "))
totales = salario*hora
print("Você ganhou %.4fR$"%totales)


interio1 = int(input("Digite um número interio: "))
interio2 = int(input("Digite um outro número interio: "))
real = float(input("Digite um número Real: "))
print("O valor dos número são respectivamente %d, %d, %.1f"%(interio1, interio2, real))