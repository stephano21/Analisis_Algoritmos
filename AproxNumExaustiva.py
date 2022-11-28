# aproximacion de soluciones
objetivo = int(input("Ingrese u numero radical a analizar: ")) #O(1)
epsilon = 0.01 #O(1)
pasos = epsilon**2#O(1)
respuesta = 0.0 #O(1)
while abs(respuesta**2-objetivo)>=epsilon and respuesta <= objetivo: #O(N)
    print(f"{abs(respuesta**2-objetivo)} {respuesta}")
    respuesta += pasos #O(1)

if ((abs(respuesta**2 - objetivo) >= epsilon)): #O(1)
    print(f"no tiene raiz exacta")
else:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}.")
