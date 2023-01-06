import random
import numpy as np
#definir los arreglos de los jugadores y la baraja

jugador1 = []
jugador2 = []
baraja=[[1,'3x+8=4x+7'], [1,'x/2+1/2=x'], [1,'7x+5=6x+6'], [1,'5-3x=x+1'], [1,'2x-7=x-6'],[2,'8-3x=10-4x'],[2,'1-2x=x-5'],[2,'2x+8=6x'],[2,'3x-5=3-x'],[2,'4x/3-2/3=x'],[3,'x/3-3=5-7x/3'],[3,'2x+7=6x-5'],[3,'x+3=12-2x'],[3,'4x-7=3x-4'],[3,'x/2+8=5x/2+2'],[4,'-2x=x-10'],[4,'2x-3=x/2+3'],[4,'-2x15=2x-1'],[4,'2(x+1)=x+6'],[4,'2-x=x/2-x'],[5,'2x-7=8-x'],[5,'-3x-1=21+x'],[5,'3x/2-15/2=0'],[5,'3x-10=15-2x'],[5,'-8x-4=-9-7x'],[6,'2x-4=14-x'],[6,'5x-10=26-x'],[6,'-3x+8=2x+2'],[6,'x/6+8=9'],[6,'x+8=20-x']]
player_data=[]
def jugar():
    print("-"*5,"[INICIO]","-"*5)
    item=[1,input("Nombre Jugador 1: "),0,0]#data player(order,nickname,score,position)
    player_data.append(item)
    item=[2,input("Nombre Jugador 2: "),0,0]#data player(order,nickname,score,position)
    player_data.append(item)
    barajar_cartas(baraja)
    print("-"*5,"[CARTAS BARAJADAS]","-"*5)
    repartir(baraja)
    print("-"*5,"[REPARTIENDO CARTAS]","-"*5)
    while True:
        if player_data[0][2]==5 or player_data[1][2]==5:break
        for turno in range(0,2):
            if len(jugador1)==0 and len(jugador2)==0: 
                barajar_cartas(baraja) 
                repartir(baraja)
            print(" "*20,f"MARCADOR\n{player_data[0][1]}: {player_data[0][2]} | Casilla:{player_data[0][3]}")
            print(f"{player_data[1][1]}: {player_data[1][2]} | Casilla:{player_data[1][3]}")
            print("\n","-"*5,f"[JUEGA {player_data[turno][1]}]","-"*5)
            print("Escoje una carta para continuar....")
            response=show_cartas(turno)#card & result_validate
            steps=validate_input(response)
            return_card(steps,turno,response[1])
            validate_move(player_data,turno)#verify position comodin or bad
            print("-"*50)
            

    
        

#devuelve las cartas a la baraja
def return_card(steps,flag,index):
    if flag==0:
        baraja.append(jugador1[index])
        jugador1.pop(index)
        move(flag,steps)

    elif flag==1:
        baraja.append(jugador2[index])
        jugador2.pop(index)
        move(flag,steps)


#update position
def move(flag,steps):
    pos_actual=player_data[flag][3]
    new_pos=pos_actual+steps
    player_data[flag][3]=new_pos

#reactualiza la posicion acorde a los comodines o trampas
def validate_move(data,flag):
    pos_act=data[flag][3]
    if pos_act==25:
        player_data[flag][3]=5
        print("Casi fue gol, retorna a casilla 5")
    elif pos_act==8:
        player_data[flag][3]=0
        print("Empezando de 0")
    elif pos_act==13:
        move(flag,2)
        print("Has avanzado dos pasos!")
    elif pos_act==24:
        player_data[flag][3]=14
        print("Fuera de juego! retrocede 10 casillas")
    elif pos_act==22:
        print("penalti")
        response=show_cartas(flag)#card & result_validate
        steps=validate_input(response)
        return_card(steps,flag,response[1])
        if steps>=3 or steps<=6:
            score_act=player_data[flag][2]
            new_score=score_act+1
            player_data[flag][2]=new_score
            print("Goool de penalti!")
        elif steps==1 or steps==2:
            player_data[flag][3]=5
            print("Atrapada por el portero, regresa a casilla 5!")
    elif pos_act>25:
        score_act=player_data[flag][2]
        new_score=score_act+1
        player_data[flag][2]=new_score
        player_data[flag][3]=0
        print("gool!")


#recibre y valida respuesta desde el usuario
def validate_input(response):
    print("-"*50,"\n","INGRESE RESPUESTA DE:")
    print(f"{response[0][1]}")
    try:
        n=int(input("==> "))
        if n != response[0][0]:
            print('Calcula bien e intenta nuevamente!')
            return validate_input(response)
        return n
    except:
        print("Ingrese datos válidos!")
        return validate_input(response)
#mostrar cartas
def show_cartas(flag):
    if flag==0:
        for i in range(len(jugador1)):
            print(f"[{i+1}] {jugador1[i][1]}")
        
        carta_select=validate_rango(jugador1)
        return jugador1[carta_select],carta_select
    elif flag==1:
        for i in range(len(jugador2)):
            print(f"[{i+1}] {jugador2[i][1]}")

        carta_select=validate_rango(jugador2)
        return jugador2[carta_select],carta_select


#validar seleccion de cartas
def validate_rango(n_cartas):
    try:
        n=int(input("==>"))
        if n>len(n_cartas) or n<1:
            print("Numero fuera de rango")
            return validate_rango(n_cartas)
        else:
            return n-1
    except:
        print("Opcion incorrecta")
        return validate_rango(n_cartas)

def repartir(baraja):
    for i in range(0,4):
        jugador1.append(baraja[i])
        baraja.pop(i)
        jugador2.append(baraja[i])
        baraja.pop(i)
    return baraja



def barajar_cartas(baraja):
    # barajando las cartas
    random.shuffle(baraja)
    random.shuffle(baraja)
    return baraja

if __name__=='__main__':
    jugar()
    for i in player_data:
        if i[2]==5:
            print(f"El ganador es {i[1]}")
    