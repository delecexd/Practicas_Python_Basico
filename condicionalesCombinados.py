#condicionales combinados

edad = int(input("digite su edad: "))

if edad>=18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")

print("fin del programa 1")

edad = int(input("digite su edad: "))

if edad>0 and edad<105:
    print("edad correcta")
    if edad>=18:
         print("es mayor de edad")
    if edad<=17:
        print("es menor de edad")
else:
    print("edad incorrecta")

print("fin del programa 2")


#poner a edad dentro de un rnago
edad = int(input("digite su edad: "))

if 0<edad<105:
    print("edad correcta")
    if edad>=18:
         print("es mayor de edad")
    if edad<=17:
        print("es menor de edad")

print("fin del programa 3 ")