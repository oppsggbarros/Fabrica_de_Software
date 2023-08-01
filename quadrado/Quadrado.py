class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
        
    def mostra_lado(self):
        self.area = self.tamanho_do_lado**2
        if self.area == self.tamanho_do_lado:
            print(self.area, "Isto é um quadrado")
        else:
            print("Isto não é um quadrado")
            
    
        