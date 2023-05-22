a=1
while a !=0:
   import math
   print("Bem vindo a calculadora!!")
   print("---------------------------------------")
   print("| Digite 1 para adição                |\n| Digite 2 para subtração             |\n| Digite 3 para divisão               |\n| Digite 4 para multiplicação         |\n| Digite 5 para volume de um objeto   |\n| Digite 6 para raiz Quadrada         |\n| Digite 7 para Área de um quadrado   |\n| Digite 8 para a média de 4 números  |\n| Digite 9 para Fatoração             |\n| Digite 10 para Exponenciação        |\n| Digite 0 para sair                  |")
   a = int(input("---------------------------------------\n"))

   if a == 1:
       print("Bem vindo a Adição")
       num1 = float(input("Digite um número: "))
       num2 = float(input("Digite outro número: "))
       result= num1+num2
       print("O resultado é %f"%result)
       continue
   if a == 2:
        print("Bem vindo a Subtração")
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        result= num1-num2
        print("O resultado é %f"%result)
        continue
   if a == 3:
        print("Bem vindo a Divisão")
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        result= num1/num2
        print("O resultado é %f"%result)
        continue
   if a == 4:
        print("Bem vindo a Multiplicação")
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        result= num1*num2
        print("O resultado é %f"%result)
        continue
   if a == 5:
        print("Bem vindo ao Volume")
        num1 = float(input("Digite o comprimento: "))
        num2 = float(input("Digite a largura: "))
        num3 = float(input("Digite a altura: "))
        result= num1*num2*num3
        print("O resultado é %f"%result)
        continue
   if a == 6:
        print("Bem vindo a Raiz quadrada")
        num1 = float(input("Digite um número: "))
        result = math.sqrt(num1)
        print("O resultado é %f"%result)
        continue
   if a == 7:
        print("Bem vindo a Área")
        num1 = float(input("Digite um número: "))
        result= num1**2
        print("O resultado é %f"%result)
        continue
   if a == 8:
        print("Bem vindo a Média de 4 números")
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        num3 = float(input("Digite outro número: "))
        num4 = float(input("Digite outro número: "))
        result= (num1+num2+num3+num4)/2
        print("O resultado é %f"%result)
        continue
   if a == 9:
        print("Bem vindo ao Fatorial")
        num1 = float(input("Digite um número: "))
        result=1
        contador=1
        while contador <= num1:
            result *= contador
            contador += 1
        print("O resultado é %.0f"%result)
        continue
   if a == 10:
        print("Bem vindo ao Exponenciação")
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite o expoente"))
        result= num1**num2
        print("O resultado é %f"%result)
        continue
   else:
        break