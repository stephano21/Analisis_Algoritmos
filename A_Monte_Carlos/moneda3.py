import random
usuario1=int(input("Ingrese\n[1] Cara \n[0] Sello \n"))
usuario2=int(input("Ingrese\n[1] Cara \n[0] Sello \n"))
usuario3=int(input("Ingrese\n[1] Cara  \n[0] Sello \n"))

maquina=random.randint(0,1)
if maquina==usuario1:
    print("Gano Ecuador <3 :3")
elif maquina==usuario2:
    print("Gano Senegal") 
elif maquina==usuario3:
    print("Gano el usuario tres") 
else:
    print("Ganó Holanda")