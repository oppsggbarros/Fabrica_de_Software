def qtd_dígitos(b):
    cont=0
    a = str(b)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
            cont = cont+1
        else:
            return len(a)
    return len(a)
while True:
    try:

        num = int(input("Digite um número: "))
        print(qtd_dígitos(num))
    except ValueError:
        print("Digite somente número inteiros!")
        continue