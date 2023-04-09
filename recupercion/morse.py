#DE CLAVE A MORSE
def conver_morse(numero_cuenta):
    valores_m=["..-.","..-",".-",".-..","-..","-.-.","...-","-.-","-."]
    res = list(map(int, str(numero_cuenta))) 
    m = len(res)
    convertido = ""
    j = 0
    while (j<m):
        espacio = ' '
        if j == 0:
            espacio = ''
        convertido = convertido+  espacio+valores_m[res[j]]
        j=j+1
    return (convertido)


#DE MORSE A CLAVE
def conver_clave(morse):
    valores_m=["..-.","..-",".-",".-..","-..","-.-.","...-","-.-","-."]
    partes = morse.split(' ')
    # construye numero
    numero = 0
    m = len(partes)
    for i in range(0,m,1):
        digito = valores_m.index(partes[i])
        numero = numero*10+digito
    return numero

#Programa principal
numero_cuenta = int(input("Ingrese numero de cuenta: "))
while numero_cuenta<1000:
    print(f'Fuera de rango, debe de ingresar solo 4 digitos')
    numero_cuenta = int(input("Ingrese numero de cuenta: "))
else:
    print("Inicia el procesamiento de clave")
    morse=conver_morse(numero_cuenta)
    print("===================================================")
    print(f'La clave morse para el digito escrito es: {morse}')
    print("")
    clave = conver_clave(morse)
    print(f'El digito de la clave morse es: {clave}')
    print("===================================================")
    