# funciones fx


# sin argumento sin retorno
def saludo():
    print("Hola que tal?")

saludo()

#sin argumento y con retorno

def suma():
    num1=3
    num2=5
    return(num1+num2)

resultado=suma()
# tambien se puede poner
# print(suma())
print(resultado)

def esmayor():
    edad=24
    if edad>=18:
        return True
    else: 
        return False
    
print(esmayor())

# con argumento y sin retorno

def saludame(name):
    print("hola", name)

saludame("Yudai")

def calculaIVA(neto):
    print(f"El precio con IVA es:, {neto*1.19}")

calculaIVA(4000)

# Con argumento y con retorno

def sumaCA(n1,n2):
   
    return(n1+n2)


def calculaIVAca(neto):
    return neto*1.19

print("El resultado es:", sumaCA(7,10))
print("El total con IVA es:", calculaIVAca(10000))




v=int(input("Ingrese el valor neto:"))
print("El total con IVA es:", calculaIVAca(v))

