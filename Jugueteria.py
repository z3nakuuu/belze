juguetes=["yo.yo", "tetris"]

def mostrarJguete():
    for j in range(len(juguetes)):
        print(f"(j+1),- (juguetes{j})")
def mostrarJ():
    print("-"*20)
    c=1
    for i in juguetes:
        print(f"(c),- (i)")
        c+=1
def agregar():
    agregar=input("ingrese juguete")
    juguetes.append(agregar)
def eliminar():  
    print("-"*20)
    mostrarJ()
    eliminar=int(input("Que juguete desea eliminar"))
    juguetes.pop(eliminar-1)
    print(f"(juguetes{eliminar-1}) fue eliminado correctamente")  
def actualizar():
    print(""*20)
    mostrarJ()
    actualizar=int(input("Que juguete desea actualizar?: "))
    juguetes[actualizar-1]=input("Ingrese el nuevo nomnbre:")

while True:
    try:
        print("-"*20)
        print("1.- Agregar Juguete")
        print("2.- Eliminar Juguete")
        print("3.-Actualizar juguete")
        print("4.- Mostrar Juguetes")
        print("5.-Salir")
        op=int(input("Seleccione una opción:"))
        match op:
            case 1:
                agregar()
            case 2:
                eliminar()
            case 3:
                actualizar()
            case 4:
                mostrarJ()
            case 5:
                print("Saliendo")
            case _:
                print("Opción inválida")
    except:
        print("solo numeros enteros")