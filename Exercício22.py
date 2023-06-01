num = int(input('Quantos eleitores terão: '))
gleissin = 0
matos = 0
christian = 0
for i in range(num):
    numero = int(input("GLEISSIN  -1\nMATOS     -2\nCHRISTIAN -3\nDigite o número do canditado há ser VOTADO: "))
    if numero == 1:
        gleissin = gleissin+1
    elif numero == 2:
        matos = matos+1
    elif numero == 3:
        christian = christian+1

total = gleissin+matos+christian
print("Quantidade Total de votos foi de %d votos"%total)
print("Votos totais do Gleissin foi %d votos"%gleissin)
print("Votos totais do Matos foi %d votos"%matos)
print("Votos totais do Christian foi %d votos"%christian)