print(" Bienvenidos al Hospital Central Metropolitano")
senior=0
junior=0

totalm=int(input("Ingrese cuantos medicos desea registrar:"))

for i in range(totalm):
        try:
            med=int(input("Ingrese el nombre del profesional médico"))       
        except NameError:
            print("El nombre debe contar con al menos 6 caracteres")
        try:
            exp=int(input("Ingrese la cantidad de años de experiencia médica"))  
            if exp>5:
                print("El médico es un Especialista Senior")
                senior+=1  
            elif exp<5:
                print("El médico registrado es un Residente Junior")
                junior+=1
        except ValueError:
            print("¡Error clínico, Ingresa un numero positivo para la experiencia!")


print(f"El total de medicos ingresados es{totalm}")
print("El hospital cuenta con", senior, "Especialistas Senior y con", junior ," Residentes junior. Sistema listo para operar")






        



