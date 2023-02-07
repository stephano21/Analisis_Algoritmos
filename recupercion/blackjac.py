import random
import numpy as np
#definir los arreglos de los jugadores y la baraja

cupier = [[random.randint(1,11),random.randint(1,11)]]
jugadores=[]
figura=['trebol','corazon negro','brillo','corazon rojo']
valor=[1,2,3,4,5,6,7,8,9,10,11,11,11]
baraja=[]
for i in figura:
    for j in valor:
        data=[i,j]
        baraja.append(data)


def jugar():
    barajar_cartas(baraja)
    repartir(baraja)
    print(jugadores)
    print(f"JUGADOR: {suma_jugador(jugadores)}")
    print(f"CUPIER: {suma_jugador(cupier)}")
    input("[S] Stop\n[C] Continuar\n==>")
    

def suma_jugador(lista):
    total=0
    for i in lista:
        total+=i[1]
    return total



def repartir(baraja):
    for i in range(0,2):
        jugadores.append(baraja[i])
        baraja.pop(i)
    return baraja



def barajar_cartas(baraja):
    # barajando las cartas
    random.shuffle(baraja)
    random.shuffle(baraja)
    return baraja

if __name__=='__main__':
    jugar()
    """ for i in player_data:
        if i[2]==5:
            print(f"El ganador es {i[1]}") """
    