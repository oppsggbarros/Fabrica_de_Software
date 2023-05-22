turno = str(input("Informe seu turno: "))
turno = turno.upper()
if turno == "M":
    print("Bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print("Boa noite")
else:
    print("Forma invalida")