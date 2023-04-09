import random

def ruleta():
  # Lista de números disponibles en la ruleta
  numeros = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
  # Seleccionamos un número al azar de la lista
  ganador = random.choice(numeros)
  
  apuesta = int(input("Apuesta en un número entre 0 y 36: "))
  
  if apuesta == ganador:
    print("Felicidades, has ganado!")
  else:
    print("Lo siento, perdiste. El número ganador fue", ganador)

# Llamamos a la función para jugar una partida de ruleta
ruleta()
