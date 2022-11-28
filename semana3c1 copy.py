#Factorial de un numero
from datetime import datetime
num =int(input("Ingrese un numero Factorial=> ")) #O 1
inicio=datetime.now()
factorial=1 #O 1
for i in range(1,num+1):#
    factorial=i*factorial
print(f"El numero factorial es {factorial}")
fin=datetime.now()
print(fin-inicio)