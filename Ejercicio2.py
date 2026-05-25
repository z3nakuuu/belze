

op=0
libros=120
while op!=6:
    try:    
        print("===MENÚ PRINCIPAL===")
        print("1. Libros disponibles")
        print("2.Realizar préstamo")
        print("3.Devolver préstamo")
        print("4.Historial de préstamos")
        print("5.Salir")        
        match op:
            case 1:
                print("La cantidad de libros disponibles es ", libros)
            case 2:
                try:
                    prest=int(input("¿Cuántos libros desea solicitar"))
                    libros-=prest
                    if prest>libros:
                        print("Lo sentimos, pero el numero que solicita es mayor al stock existente")
                    elif libros==0:
                        print("Ya no quedan libros disponibles en Stock")
                except:
                    print("Ingrese solo numeros enteros")        
            case 3:
                try:
                    devo=int(input("¿Cuántos libros va a devolver?"))
                    libros+=devo
                    if devo+libros>120:
                        print("Lo sentimos, no se puede ingresar mas libros al stock existente")
                    elif devo==0:
                        print("solo puede devolver numeros mayores a 0")
                except:
                    print("solo puede ingresar numeros enteros")
            case 4:
                print("Historial de préstamos y devoluciones")
                print("durante la sesión solicitaste ", prest , "libros")
                print("y devolviste ", devo , "libros ")
                print(" el stock que queda disponible en biblioteca es ", libros)
                      
            case 5:
                print("Gracias por utilizar nuestro software, hasta la próxima")
                op=5
    except:
        print("Error, por favor ingrese una opción válida")            
