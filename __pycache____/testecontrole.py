from Controle import *
while True:
    a = int(input())
    if a == 1:
        controle = Controle()
        controle.mostrar_status()  
    elif a == 2:
        controle = Controle()
        controle.aumentar_volume()
        controle.mostrar_status()  
    elif a == 3:
        controle = Controle()
        controle.trocar_canal(5)
        controle.mostrar_status()  
    elif a == 4:
        controle = Controle()
        controle.diminuir_volume()
        controle.mostrar_status()  
    elif a == 5:
        controle = Controle()
        controle.carregar_bateria()
        controle.mostrar_status()  
