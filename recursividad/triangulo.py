def cuadro(n):
    if n==0:
        return"\n"
    else:
        return "*"*n+"\n"+cuadro(n-1)
dimencion = int(input("Ingrese la dimencion del cuadrado: "))
print(cuadro(dimencion))