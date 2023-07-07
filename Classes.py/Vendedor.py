class Vendedor():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas


    def vendeu(self, vendas):
        self.vendas = vendas
        print(self.vendas)
    def bateu_metas(self, metas):
        if self.vendas > metas:
            print("Bateu a meta")
        else:
            print("Não bateu a meta")
vendedor1=Vendedor('Gabriel', 1000)
print(vendedor1.nome)
vendedor1.bateu_metas(1001)
