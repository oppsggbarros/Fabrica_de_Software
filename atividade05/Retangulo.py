class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudar_valor(self, ladoAA, ladoBB):
        self.ladoAA = ladoAA
        self.ladoBB = ladoBB
    
    def calcular_area(self):
        self.area = self.ladoA*self.ladoB
        print(f"A área do retangulo é {self.area}")

    def calcular_perimetro(self):
        self.perimetro = self.ladoA * 2 + self.ladoB*2
        print(f"E o perímetro é {self.perimetro}")