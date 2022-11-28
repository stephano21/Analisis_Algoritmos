def suma(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    else:
        return 1+suma(n1,n2-1)


print(suma(int(input("Ingrese un numero")),int(input("Ingrese un numero"))))
