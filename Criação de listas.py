lista = [10, 20, 30, 40]
print(lista)
print(type(lista))

b = ["Python", 3.5, True, 1, ["sasd", 89.7]]
print(b[:4])
print(type(b))
print(len(b))
print("Arara" not in b)
print(89.7 in b)
lista1 = [1,3,5]
lista2 = [2,4,6]
print(lista1+lista2)
print(max(lista1))#Maior número
print(min(lista1))#Menor número
print(sum(lista1))#Soma

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[:3])
print(uma_lista[:])
print(uma_lista[0:6])
frutas = ["banana", "maçã", "cereja"]
frutas[0] = "pera"
del frutas[0]
print(frutas)

list = ["flor", "Azul", [ 1, 'casa']]#é mutável
list[2][1] = "escola"
list[2] = [True], 
list.append(5)#Adiciona no final da lista

print(list)

a = [1,2,3,4,5,6,4]
a.insert(2,100)
a.pop(-1)
print(a)
