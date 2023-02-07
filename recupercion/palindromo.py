
def palindromo(cadena):
    print(cadena)
    if (len(cadena)==0):
        return "La palabra ingresada, ES PALINDROMA"
    else:
        if (cadena[0]==cadena[-1]):
            return palindromo(cadena[1:-1])
        else:
            return "NO ES PALINDROMA"
cadena =input("INGRESE LA FRASE A VERIFICAR: ")
cadena =cadena.lower()
cadena =cadena.replace(" ","")
print(cadena)
print(palindromo(cadena))