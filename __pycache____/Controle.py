class Controle:
    def __init__(self):
        self.bateria = 100
        self.volume = 50
        self.canal = 1

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("O volume já está no máximo!")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("O volume já está no mínimo!")

    def trocar_canal(self, canal):
        if canal >= 1 and canal <= 100:
            self.canal = canal
        else:
            print("Canal inválido!")

    def mostrar_status(self):
        print("Bateria:", self.bateria)
        print("Volume:", self.volume)
        print("Canal:", self.canal)

    def carregar_bateria(self):
        self.bateria = 100
        print("A bateria foi recarregada.")



