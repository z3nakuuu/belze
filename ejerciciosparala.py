op=0
cantpersonas=0
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
            cantpersonas+=1
            total+=1000
        case 2:
            print("pagando el precio de adulto")
            cantpersonas+=1
            total+=3000
        case 3:
            print("pagando el precio adulto mayor")
            cantpersonas+=1
            total+=1500
        case 4:
            print("Saliendo del menu")
            op=4
        case _:
            print("Opción inválida")
