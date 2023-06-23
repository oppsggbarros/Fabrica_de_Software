import os

def valorPagamento(x,y):
    juros=(0.1*y)/100
    multa=(x*0.03)
    jurostotal=((x*juros)+multa)+x
    return jurostotal

prestações=[]
diasAtraso=[]
valorFinal=[]

while True:
    try:
        a=float(input("Digite o valor a ser pago pela prestação: "))
        b=int(input("Digite o número de dias de atraso: "))
    except ValueError:
        os.system("cls")
        print("Erro! Digite somente números inteiros para os dias, e demais números para o valor da prestação.")
        os.system("pause")
        os.system("cls")
    except:
        os.system("cls")
        print("Erro desconhecido.")
        os.system("pause")
        os.system("cls")
    else:
        if a==0:
            os.system("cls")
            break
        elif a>0 and b>=0:
            os.system("pause")
            os.system("cls")
            prestações.append(a)
            diasAtraso.append(b)
            c=valorPagamento(a,b)
            valorFinal.append(c)
            continue
        else:
            os.system("cls")
            print("Valor não adicionado por conter números negativos. Por favor, tente novamente.")
            os.system("pause")
            os.system("cls")

print("------------------------------------------------------------------------------ Relatório do Dia ------------------------------------------------------------------------------\nValores das Prestações em Ordem:")
for i in prestações:
    print("{:.2f}R$".format(i))
print("\nDias de Atraso em Ordem:")
for i in diasAtraso:
    print(i)
print("\nValores finais a serem pagados:")
for i in valorFinal:
    print("{:.2f}R$".format(i))
