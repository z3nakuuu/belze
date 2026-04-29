op=0
cantpersonas=0
cantniños=0
cantadultos=0
cantviejitos=0
total=0
while op!=4:
    print('''
        1.Niño (1-17) 1000
        2.Adulto(18-64) 3000
        3.Adulto mayor(+65) 1500
        4. Salir''')
    op=int(input("Seleccione una opción"))
    match op:
        case 1:
            print("Pagando el precio de niño")
            print(f"la cantidad de niños es {cantniños}")
            cantpersonas+=1
            cantniños+=1
            total+=1000
        case 2:
            print("pagando el precio de adulto")
            print(f"la cantidad de adultos es {cantadultos}")
            cantpersonas+=1
            cantadultos+=1
            total+=3000
        case 3:
            print("pagando el precio adulto mayor")
            print(f"la cantidad de adultos mayores es {cantviejitos}")
            cantpersonas+=1
            cantviejitos+=1
            total+=1500
        case 4:
            print("Saliendo del menu")
            print(f"el total a pagar es {total}")
            print(f"la cantidad de personas es { cantpersonas}")
            op=4
        case _:
            print("Opción inválida")
