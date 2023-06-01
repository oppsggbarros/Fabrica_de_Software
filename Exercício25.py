maior = -1
menor = 99999999
for i in range(5):
    passeio = int(input("Quantos carros estvão em passeio em 1999: "))
    acidentes = int(input("Quantos acidentes de trânsitocom vítimas teve em 1999: "))
    if acidentes>maior:
        maior=acidentes
        cidademaior=i+1
    if acidentes<menor:
        menor = acidentes
        cidademenor=i+1
    

print(cidademaior, i)
print(cidademenor, i)