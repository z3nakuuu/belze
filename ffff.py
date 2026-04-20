entrenador=" takato Guilmon "

dign1=6

entrenador2="ruki renamon"
dign2=7

#if dign2<=6:
#    print("Puede acceder a la liga digimon")
#else:
 #   print("tiene mas digimons de los necesarios")


# print(len(entrenador))

#print("El entrenador", entrenador, "tiene", dign1, "digimons")
#print("El entrenador", entrenador2 "tiene", dign2, "digimons")
#print(f"El entrenador {entrenador2} tiene {dign1} digimons")


# print(f"Hola {entrenador}"*3)
# -3 -2 -1
# name="ana"
# 012
print(entrenador.strip())
print(entrenador.lower().strip())
print(entrenador2.upper())
print(entrenador2.replace("renamon", "grant"))
print(entrenador2.find("renamon"))
print(entrenador2.split())

# pedir la clave al usario y verificar que sea SHAZAM independiente sea mayuscula

pasw="shazam"
code=input("ingrese la contraseña: ")

if pasw==code.upper():
    print("Bienvenido al systema")
else:
    print("error clave invalida")


#crear un nombre de usuario y verificar que su clave sea largo entre
# 4 y 10 caracteres

user=input("ingrese su nombre de usuario")
if len(user)<4:
    print("Muy pocos caracteres, use al menos cuatro ")
elif len (user)>10:
    print("Tiene demasiados caracteres")
else:
    print("usuario creado correctamente")

# crean un pin y que tenga exactamente 4 digitos

code=input("ingrese su contraseña")
if len(code)==4
    print("contraseña creada exitosamente")
else:
    print("error, su contraseña debe tener 4 digitos")
    













