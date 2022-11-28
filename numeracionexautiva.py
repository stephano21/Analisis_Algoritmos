objetivo = int(input("Ingrese u numero radical a analizar: "))
respuesta = 0
while (respuesta**2 < objetivo):
    print(respuesta)
    respuesta += 1

if (respuesta**2 == objetivo):
    print(f"La raiz cuadrada de {objetivo} es {respuesta}.")
else:
    print(f"no tiene raiz exacta")
