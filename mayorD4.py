n1 = int(input("Ingrese un numero 1 "))
n2 = int(input("Ingrese un numero 2 "))
n3 = int(input("Ingrese un numero 3 "))
n4 = int(input("Ingrese un numero 4 "))

if (n1 > n2 and n1 > n3 and n1 > n4):
    print(f"El numero {n1} es el mayor")
elif (n2 > n1 and n2 > n3 and n2 > n4):
    print(f"El numero {n2} es el mayor")
elif (n3 > n1 and n3 > n2 and n3 > n4):
    print(f"El numero {n3} es el mayor")
else:
    print(f"El numero {n4} es el mayor")
