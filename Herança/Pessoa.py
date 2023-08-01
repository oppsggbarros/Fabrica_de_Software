class Pessoa:
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    def relatorio(self):
        print()
        print()
        print()
        print()
        print()

class Aluno(Pessoa):
    def __init__(self,mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade
        super().relatorio
        print("Mensalidade: ", self.mensalidade)
        
