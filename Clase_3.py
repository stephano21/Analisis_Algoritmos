#1 Mayor de dos numeros

N1 = int(input("Imgrese el numero 1 "))
N2 = int(input("Imgrese el numero 2 "))

if (N1 > N2):
    print(f"El numero mayor es {N1} ")
elif (N2 > N1):
    print(f"El numero mayor es {N2} ")
else:
    print("Los numeros son iguales")

#2 Celcius a Farentheith

print("[1] Celcius a Fahreinth\n[2] Fahreinth a Celcius")
op= int(input("Ingrese una opcion =>"))
if op==1:
    C=float(input("Grados Celcius: "))
    F= C*(9/5)+32
    print(f"Los grados Fahreinth son {F}")
elif op==2:
    F=float(input("Grados Fahreinth: "))
    C=(F-32)*(5/9)
    print(f"Los grados Celcius son {C}")
else:
    print("Ingrese una opcion Válida")

#3 mayor de 4 numeros

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

#4 Mayor edad

edad = int(input("Ingrese su edad => "))
study = input("Estudia Analisi de algoritmos (S/N)")
study = study.lower()
if edad > 18 and study == "s":
    print("Es mayor de edad y pasa la materia +1 Biela")
elif edad<18 and study=="s":
    print("Es menor de edad y tiene un dulce")
elif edad>18 and study=="n":
    print("Es mayor de edad y se queda")
else:
    print("Es menor de edad y Se queda")