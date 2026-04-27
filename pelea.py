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
        print(f" el hp de {p2} es {hp2}")
    else:
        print(f"turno de {p2}")
        atk=random.randint(7,18)
        print(f" el {p2} ataca con {atk} ")
        HP1-=atk
        print(f" el hp de {p1} es {hp1}")
    turno+=1
    print(p1, "█"*hp1)
    print(p2, "█"*hp2)
if HP1>HP2:
    print("el ganador es ", p1)
else:
    print("el ganador es ", p2)