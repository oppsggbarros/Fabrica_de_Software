names = ["leticia", "joão", "pedro"]
for n in names:
    
    if n == "joão":
        continue
    print(n)
letras = "abc"
for n in letras:
    print(n)
for x in range(2,10,6):
    print(x)
for i in range(5):
    for j in range(6):
        print(i,j)

for l in range(1,11):
    print("------------------------")
    for l2 in range(1,11):
        total = l*l2
        print(l, "x", l2, "=", total)
for l in range(0,101,2):
    print(l)
a= int(input("Informe um número: "))
b= int(input("Informe um número: "))
for x in range(a,b):
    print(x)