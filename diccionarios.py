# uso y explicación de diccionarios

# alumno={
#       "nombre":"Shinji Ikari",
#         "edad":"14",
#         "carrera":"Piloto"

# }

# print(alumno)
# print(alumno["carrera"])
# for key, value in alumno.items():
#     print(key, value)

# alumno["email"]="shinji@nerv.com" #actualizar datos
# del alumno["edad"] #borrar datos

productos={
    1:{"nombre":"control inalambrico",
       "categoria":"electronica",
       "precio":45000},
    2:{"nombre":"pilas recargables",
       "categoria":"insumos",
       "precio":5000},
    3:{"nombre":"pasta termica",
       "categoria":"commputación",
       "precio":7000},
}

print(productos[2]["categoria"]) # Esto es un ejemplo, puedes cambiar los valores para q printees lo q necesites

# Tarea
# modificar el programa del carrito de compras para poder utilizarlo con listas.....
# el producto debe tener nombre y precio



productos=[]
while True:

    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. eliminar producto")
    print("4. Actualizar el producto")
    print("5. salir")
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
           nombre=input("Ingrese el nombre del producto")
           precio=int(input("Ingrese el precio del producto"))
           new={"nombre":nombre,"precio":precio}
           productos.append(new)
        case 2:
            print(productos)
        case 3:
            print("")
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion invalida")