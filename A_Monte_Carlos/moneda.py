import random
usuario=int(input("Ingrese\n[1] Cara \n[0] Sello"))
maquina=random.randint(0,1)
if maquina==usuario:
    print("Gano el usuario")
else:
    print("Ganó la maquina")