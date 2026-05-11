# haremos un menu
# con try y except

#  op=0
#  total=0 #acumulador, ya que se ponen valores que se van sumando
# cantProd=0 # contador
#  while op!=4
#     try:
#         print("1.- Radio stereo sony $70.000")
#         print("2.- LGTV 55 pulgadas super gamer $500.000" )
#         print("3.- PS5 $580.000")
#         print("4.- Salir")
#         print("Seleccione una opción")
#         op=int(input())
#         match op:
#             case 1:
#                 print("el precio a pagar es ", 70000*1.19)
#                 total+=70000*1.19
#                 cantProd+=1
#             case 2:
#                 print("el precio a pagar es ", 500000*1.19)
#                 total+=500000*1.19
#                 cantProd+=1
#             case 3:
#                 print("el precio a pagar es ", 580000*1.19)
#                 total+=580000*1.19
#                 cantProd+=1
#             case 4:
#                 print("Su total a pagar es ", total)
#                 print(" su total de productos es ", cantProd)
#             case _:
#                 print("opcion invalida")
#     except:
#         print("Ingrese solo los numeros opcionales")

# ejemplo de validacion

porc=float(input("Ingrese el porcentaje de viejos en su comunda"))

if porc>0 and porc<100:
    print("Porcentaje correcto")
else: 
    print("porcentaje fuera de rango")


