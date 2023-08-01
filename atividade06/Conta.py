class Conta:
    def __init__(self,nome, cpf, saldo, senha):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.senha = senha

    def depositar(self,saldo1):
        self.saldo1 = saldo1
        self.__saldo = self.__saldo + self.saldo1