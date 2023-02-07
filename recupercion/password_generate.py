#Contraseña aleatoria, el join sirve para juntar un vector en una cadena.
import random
mayuscula = ['A','B','C','D','E','F']
minuscula = ['a','b','c','d','e','f']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['*','#','$','&','@','_']
caracter = mayuscula+minuscula+numeros+simbolos
longitud = 10
contraseña = []
for i in range (longitud):
    cadena = random.choice(caracter)
    contraseña.append(cadena)
print ('Su contraseña es ' + ''.join(contraseña))