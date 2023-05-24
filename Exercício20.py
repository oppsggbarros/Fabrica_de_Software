
id = []
listnome = []
listsobbrenome = []
listbairro = []
listcidade = []
listestado = [] 
listpais = []
listfone  = []
listcpf = []
listpeso = []
listaltura = []
listcartão = []
listemail = []
listcep = []
listmedia = []
listsérie = []
listclasse = []
listsexo = []
listcor = []
listendereço = []
listidade = []
cont=0
listmatricula = []
while True:
    print("Selecione a opção")
    op = int(input("1-Cadastro\n2-Consulta\n0-Sair\n"))
    if op == 1:

        nome = input("Informe seu nome: ")
        listnome.append(nome)
        sobrenome = input("Informe seu sobrenome: ")
        listsobbrenome.append(sobrenome)
        endereço = input("Informe seu Endereço: ")
        listendereço.append(endereço)
        bairro = input("Informe seu Bairro: ")
        listbairro.append(bairro)
        cidade = input("Informe seu Cidade: ")
        listcidade.append(cidade)
        estado = input("Informe seu Estado: ")
        listestado.append(estado)
        pais = input("Informe seu País: ")
        listpais.append(pais)
        fone = int(input("Informe seu Fone: "))
        listfone.append(fone)
        cpf = int(input("Informe seu CPF: "))
        listcpf.append(cpf)
        peso = float(input("Informe seu Peso: "))
        listpeso.append(peso)
        altura = float(input("Informe sua Altura: "))
        listaltura.append(altura)
        idade = int(input("Informe seu idade: "))
        listidade.append(idade)
        cartão = int(input("Informe seu Número do cartão: "))
        listcartão.append(cartão)
        email = input("Informe seu email: ")
        listemail.append(email)
        cep = int(input("Informe seu CEP: "))
        listcep.append(cep)
        nota1 = float(input("Informe seu nota 1: "))
        nota2 = float(input("Informe seu nota 2: "))
        nota3 = float(input("Informe seu nota 3: "))
        nota4 = float(input("Informe seu nota 4: "))
        media=(nota1+nota2+nota3+nota4)/4
        listmedia.append(media)
        série = input("Informe sua Série: ")
        listsérie.append(série)
        classe = input("Informe seu Classe: ")
        listclasse.append(classe)
        sexo= input("Informe seu Sexo: ")
        listsexo.append(sexo)
        cor = input("Informe sua Cor: ")
        listcor.append(cor)
        cont=cont+1
        listmatricula.append(cont)
    if op==2:
        busca = int(input("Digite a matrícula"))
        print(listmatricula[busca-1])
        print(listnome[busca-1])
        print(listsobbrenome[busca-1])
        print(listbairro[busca-1])
        print(listcidade[busca-1])
        print(listestado[busca-1])
        print(listpais[busca-1])
        print(listfone[busca-1])
        print(listcpf[busca-1])
        print(listpeso[busca-1])
        print(listaltura[busca-1])
        print(listcartão[busca-1])
        print(listemail[busca-1])
        print(listcep[busca-1])
        print(listmedia[busca-1])
        print(listsérie[busca-1])
        print(listclasse[busca-1])
        print(listsexo[busca-1])
        print(listcor[busca-1])
        print(listendereço[busca-1])
        print(listidade[busca-1])

    if op == 0:
        break
    if op == 3:
        (listnome.pop(busca-1))
        (listsobbrenome.pop(busca-1))
        (listbairro.pop(busca-1))
        (listcidade.pop(busca-1))
        (listestado.pop(busca-1))
        (listpais.pop(busca-1))
        (listfone.pop(busca-1))
        (listcpf.pop(busca-1))
        (listpeso.pop(busca-1))
        (listaltura.pop(busca-1))
        (listcartão.pop(busca-1))
        (listemail.pop(busca-1))
        (listcep.pop(busca-1))
        (listmedia.pop(busca-1))
        (listsérie.pop(busca-1))
        (listclasse.pop(busca-1))
        (listsexo.pop(busca-1))
        (listcor.pop(busca-1))
        (listendereço.pop(busca-1))
        (listidade.pop(busca-1))
