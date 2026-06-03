def calculo(precio,descuento):
    return precio -(precio*descuento/100)
calculo(20500,22) #20500 es el precio y 22 representa 22% de descuento
print("El valor con descuento es:", calculo(20500,22))

# actividad 3.3.3

numeros=input("Ingrese tus numeros, separarlos con espacios entre las comas")


def paresImpares(numeros):
    listanum= numeros.split()

for a in range(len(listanum)):
    listanum[a] = int(listanum[a])

pares=[]
impares=[]

for i in (listanum):
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print("Los numeros pares son:", pares)
print("Los numeros impares son:", impares)


# Cree una funcion para pedir notas y ponerlas en el argumento
# para sacar el promedio


notas=int(input("Ponga sus notas"))
prom=[]
for n in range(notas): 
    nota=int(input(f"Ingrese la nota {n+1}: "))
    prom.append(nota)

def calcularProm(no):
    return sum(no)/len(no)


print("el promedio es", calcularProm(prom), prom)



    

