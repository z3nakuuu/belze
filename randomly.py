# import random

#strike=random.randint(10,70)

#if strike>50:
 #   print("Its a critical hit. Damage ", strike)
#else:
 #   print("Its not very effective. Damage", strike)








# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear 
# y la distancia varia entre 60 y 190 metros
# mostrar al final, el golpe mas fuerte

#import random
#import time

#player1=random.randint(60,190)
#player2=random.randint(60,190)
#player3=random.randint(60,190)
#time.sleep(2)
#print(f"el jugador 1 golpeo la pelota a {player1} metros" )
#print(f"el jugador 2 golpeo la pelota a {player2} metros" )
#print(f"el jugador 3 golpeo la pelota a {player3} metros" )

#if player1>player2 and player1>player3:
 #   print("el jugador uno hizo el tiro mas lejano")
#elif player2>player3:
 #   print("el jugador dos hizo el tiro mas lejano")
#else:
 #   print("el jugador tres hizo el tiro mas lejano")



#killer instinc

# dos peleadores se piden al inicio de la pelea
# cada peleador inicia con 100 de HP
# se debe hacer una pelea por turnos
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2 
# tiene su hp en 0
# se debe mostrar el ganador al final 
# BONUS  mostrar las barras de energia de cada peleador

import random
import time



p1=input("ingrese el nombre del peleador 1")
p2=input("ingrese el nombre del peleador 2")
HP1=100
HP2=100
turno=random.randint(1,2)

while HP1>0 and HP2>0:
    if turno %2==0:
        print(f"turno de {p1}")
        atk=random.randint(7,18)
        print(f" el {p1} ataca con {atk} ")
        HP2-=atk
        print(f" el hp de {p2} es {HP2}")
    else:
        print(f"turno de {p2}")
        atk=random.randint(7,18)
        print(f" el {p2} ataca con {atk} ")
        HP1-=atk
        print(f" el hp de {p1} es {HP1}")
    turno+=1
    time.sleep(2)
    print(p1, "█"*HP1)
    print(p2, "█"*HP2)
if HP1>HP2:
    print(f"el ganador es: {p1}")
else:
    print(f"el ganador es: {p2}")
          







