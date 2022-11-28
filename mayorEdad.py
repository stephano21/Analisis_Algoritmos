
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

