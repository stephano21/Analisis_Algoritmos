import random
lista=["piedra","papel","tijera"]

ratingM=0
ratingU=0
intentos=1
while intentos<=5:
    print("-"*5,f"[{intentos}]","-"*5)
    usuario=int(input(f"Ingrese una opcion:\n[1] Piedra\n[2] Papel\n[3] Tijera\n==>"))
    maquina=random.choice(lista)
    print(lista[int(usuario)-1])
    if maquina==lista[0] and lista[usuario-1]==lista[2]:
        print(maquina," Mata a ", lista[usuario-1])
        print("Gano la maquina")
        ratingM+=1
    elif maquina==lista[2] and lista[usuario-1]==lista[0]:
        print(lista[usuario-1], "Mata a",maquina)
        print("Gano el usuario")
        ratingU+=1
    elif maquina==lista[1] and lista[usuario-1]==lista[0]:
        print(maquina, "Mata a",lista[usuario-1])
        print("Gano el Maquina")
        ratingM+=1
    elif maquina==lista[0] and lista[usuario-1]==lista[1]:
        print(lista[usuario-1], "Mata a",maquina)
        print("Gano el usuario")
        ratingU+=1
    elif maquina==lista[1] and lista[usuario-1]==lista[2]:
        print(lista[usuario-1], "Mata a",maquina)
        print("Gano el usuario")
        ratingU+=1
    elif maquina==lista[2] and lista[usuario-1]==lista[1]:
        print(maquina, "Mata a",lista[usuario-1])
        print("Gano la maquina")
        ratingM+=1
    else: 
        print(maquina, lista[usuario-1])
        print("Empate")
    intentos+=1

print(f"Maquina:{ratingM} \nUsuario:{ratingU}")

