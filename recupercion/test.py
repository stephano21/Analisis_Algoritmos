#pozo millonario
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
    k = k + 1