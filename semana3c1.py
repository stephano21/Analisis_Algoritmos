#1 Factorial de un numero

from datetime import datetime


num =int(input("Ingrese un numero Factorial=> ")) #O 1
inicio=datetime.now()
factorial=1 #O 1
for i in range(num,0,-1):#for i in range(1,num+1): for de forma descendente y ascendente
    factorial=i*factorial
print(f"El numero factorial es {factorial}")
fin=datetime.now()
print(fin-inicio)

#2 fibonnacci
a=0#O(1)
b=1#O(1)
numero=int(input("Numero "))#O(1)
for i in range(1,numero+1):#O(N)[
    suma=a+b #O(1)
    a=b#O(1)
    b=suma#O(1)]
print(suma)#O(N)
#Ts=5+3N => O(N)   ORDEN DE COMPLEJIDAD LINEAL