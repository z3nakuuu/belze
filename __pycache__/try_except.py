while True:
    try:
        edad=int(input("Ingrese su edad: "))
        #salta a la linea 6, donde esta except para manejar el error
        print("su edad es ",  edad)
        break
    except ValueError as e: #se puede utilizar cualquier variable, usualmente es una e
        print("solo se aceptan numeros enteros ")
        print(e)


for i in range(10):
    n1=int(input("Ingrese su numero: "))
    if n1%2!=0:
        break

# ingrese numeros indefinidamente 
#  hasta que ponga el numero 0
#  Sumelos y muestre el total

num=0
while True:
    try:
        n1=int(input("Ingrese su numero: "))
        num+=n1
        if n1==0:
            break
    except:
            print("solo numeros enteros")


print("el total es ", num)



    




