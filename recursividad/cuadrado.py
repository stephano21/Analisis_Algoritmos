def cuadrado(copia,n):
    if n==0:
        return ""
    else:
        print("*"*copia)
        return cuadrado(copia, n-1)

n=int(input("Ingrese a dimencion del cuadro: "))
cuadrado(n,n)