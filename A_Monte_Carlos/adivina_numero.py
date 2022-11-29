import random
def numero():
    x=int(input("Ingrese un numero: "))
    return x


num=numero()
maquina=random.randint(1,100)
while True:
    if num<maquina:
        print("Ingrese un numero mayor")
        num=numero()
    elif num>maquina:
        print("Ingrese un numero menor")
        num=numero()
    else:
        print("Gano")
        exit()