""" #pozo millonario
import numpy as np
import random as rnd
# INGRESO
n = int(input('seleccionar:'))
m = int(input('de cuantos:' ))
# PROCEDIMIENTO
# Ninguno seleccionado
tabla = np.zeros(m+1,dtype=int)
# sorteando sin repetir
i = 1
while not(i>n):
    sorteado = int(rnd.random()*m)+1
    if (tabla[sorteado]==0):
        tabla[sorteado] = 1
        i = i + 1
#SALIDA
k = 1
print('Los numeros de la tabla son:')
while not(k>m):
    if (tabla[k]==1):
        print(k)
    k = k + 1 """
import numpy as np
import random as rnd

# INGRESO
n = int(input('¿cuántos jugadores?: '))
m = int(input('¿cuántas rondas?: '))

gana    = np.zeros(n+1, dtype=int)
apuesta = np.zeros(n+1, dtype=int)

ronda = 1
while (ronda<=m):

    # Ingreso de apuestas
    j = 1
    while (j<=n):
        print('jugador (',j,') ')
        apuesta[j] = int(input('  número apostado: '))
        j = j + 1

    ruleta = int(rnd.random()*37)+1
    print('Número ruleta: ', ruleta)

    # Revisa ganadores
    j = 1
    while (j<=n):
        if (ruleta==apuesta[j]):
            gana[j] = gana[j]+1   
        j = j + 1
         
    ronda = ronda + 1

# SALIDA
print('Los resultados son:')
j = 1
while (j<=n):
    print(' jugador(',j,') ganó ',gana[j],' veces \n')
    j = j + 1