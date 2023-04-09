import random 

  

# Función para dibujar los dados 

def dibujardado(num):
	print("-"*3)
	for i in range(3):
		for j in range(3):
			if num==1:
				if i==1 and j ==1:
					print("*",end="")
				else:print(" ",end="")
			if num==2:
				if (i==1 and j==0)or(i==1 and j==2):
					print("*",end="")
				else:print(" ",end="")
			if num==3:
				if (i==0 and j==0) or (i==1 and j==1) or (i==2 and j==2):
					print("*",end="")
				else:print(" ",end="")
			if num==4:
				if (i==0 and j==0) or (i==0 and j==2) or (i==2 and j==0) or (i==2 and j==2):
					print("*",end="")
				else:print(" ",end="")
			if num==5:
				if(i==0 and j==0) or (i==0 and j==2) or(i==1 and j==1) or (i==2 and j==0)or(i==2 and j==2):
				    print('*',end='')
				else:print(" ",end="")
			if num==6:
				if(i==0 and j==0)or (i==0 and j==1) or (i==0 and j==2) or(i==1 and j==0) or(i==1 and j==1)or(i==1 and j==2) or (i==2 and j==0)or (i==2 and j==1)or(i==2 and j==2):
				    print('*',end='')
				else:print(" ",end="")
		print("")
	print("-"*3)

  

# Lista de jugadores 

jugadores = [ 

    {"nombre": "Jugador 1", "dinero": 1500, "posicion": 1}, 

    {"nombre": "Jugador 2", "dinero": 1500, "posicion": 1}, 

    {"nombre": "Jugador 3", "dinero": 1500, "posicion": 1}, 

    {"nombre": "Jugador 4", "dinero": 1500, "posicion": 1} 

] 

  

# Lista de casillas del Monopoly 

casillas = [ 

    "Salida", "Avenida Mediterráneo", "Caja de Comunidad", "Avenida Báltica", 

    "Impuesto de Lujo", "Estación de Ferrocarril Reading", "Calle Oriental", 

    "Casualidad", "Avenida Vermont", "Avenida Connecticut", "Cárcel",  

    "Avenida San Carlos", "Servicio Público Electricidad", "Avenida Estados", 

    "Avenida Virginia", "Estación de Ferrocarril Pensilvania", "Plaza de St. James", 

    "Caja de Comunidad", "Avenida Tennessee", "Avenida Nueva York", "Parada Libre", 

    "Avenida Kentucky", "Casualidad", "Avenida Indiana", "Avenida Illinois", 

    "Estación de Ferrocarril B. & O." 

] 

  

# Función para calcular el siguiente turno 

def siguiente_turno(jugador): 

    # Lanzar los dados 

    dado1 = random.randint(1, 6) 

    dado2 = random.randint(1, 6) 

    dibujardado(dado1)
    dibujardado(dado2) 

    # Mover al jugador a la siguiente posición 

    jugador["posicion"] = (jugador["posicion"] + dado1 + dado2) % 24 

    # Si el jugador cae en una casilla de Casualidad, debe pagar $100 a otro jugador aleatorio 

    if jugador["posicion"] in [4, 10, 16]: 

        otro_jugador = random.choice([j for j in jugadores if j != jugador]) 

        jugador["dinero"] -= 100 

        otro_jugador["dinero"] += 100 

    # Si el jugador cae en la casilla de Impuesto de Lujo, debe pagar $75 

    if jugador["posicion"] == 5: 

        jugador["dinero"] -= 75 

    # Si el jugador cae en una estación de ferrocarril o servicio público, debe pagar $50 por cada una que tenga otro jugador 

    if jugador["posicion"] in [6, 16]: 

        for j in jugadores: 

            if j != jugador and j["posicion"] == jugador["posicion"]: 

                jugador["dinero"] -= 50 

                j["dinero"] += 50 

    # Si el jugador cae en la cárcel, pierde un turno 

    if jugador["posicion"] == 10: 

        return 

siguiente_turno(jugadores[0])