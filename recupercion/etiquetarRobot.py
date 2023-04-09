import random
import string
def nrobot(size):
    nombre=[]
    mayus=[i for i in string.ascii_uppercase]
    min=[i for i in string.ascii_lowercase]
    num=[str(i) for i in range(10)]
    print(mayus)
    print(min)
    print(num)
    caracteres=mayus+min+num
    for i in range(size):
        nombre.append(random.choice(caracteres))
    return nombre



newName=nrobot(int(input("Longitud del nombre: ")))
print('El nombre es:'+''.join(newName))
