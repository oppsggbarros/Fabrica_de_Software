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
