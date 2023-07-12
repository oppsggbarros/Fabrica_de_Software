class Conta:
    def __init__ (self,agencia, conta, nome, fone, saldo, cpf):
        
        self.agencia = agencia
        self.conta = conta
        self.nome = nome
        self.fone = fone
        self.saldo = saldo
        self.cpf = cpf

    def cadastro (self, agencia1, conta1, nome1, fone1, saldo1, cpf1):
        self.saldo = saldo1
        self.agencia = agencia1
        self.conta = conta1
        self.nome = nome1
        self.fone = fone1
        self.cpf = cpf1
        
    def saque(self, saquetirar):
        self.saquetirar = saquetirar
        if self.saquetirar > 0 and self.saquetirar < self.saldo:
            self.saquetirar -= self.saldo
            self.saquetirar = self.saquetirar * (-1)
            print(f"{self.nome} o saque que você tinha {self.saldo} sobrou: {self.saquetirar} e retirou {saquetirar}")
            return
        else:
            print("Você não tem Dinheiro o suficiente para sacar")
            return
    def depositar(self, deposito):
        self.deposito = deposito
        if self.deposito <= 0:
            print("Deposite um valor acima de 0")
            return
        else:
            self.deposito += self.saldo
            print(f"{self.nome} o deposito de {deposito} foi adicionado com sucesso\nTotal: {self.deposito}")
            return