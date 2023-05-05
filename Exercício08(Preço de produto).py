nome = input("Insira o Nome do produto: \n")
quantidade = int(input("Insira a quantidade do produto: \n"))
valor = float(input("Insira o valor do produto: \n"))
desconto = int(input("Insira o desconto: \n"))
valor_do_produto = valor*quantidade
total = valor_do_produto-valor_do_produto*(desconto/100)
print("Nome do produto:", nome, "\nValor Total do produto:", total)