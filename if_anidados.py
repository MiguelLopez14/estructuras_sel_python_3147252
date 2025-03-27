'''
if anidados
Estructuras Selectivas
que se encuentran dentro
de otro if
Syntax:

if condicion:
    if condicion:
        if condicion:
            bloque instr
        else:
            if condicion:
                bloque de intr
            else:
                bloque de intr
else:
    bloque de intrucciones
    
'''

# Ejemplo 1:
# Modificacion del ejercicio de votacion
# ahora solo puede votar si es mayor de edad
# pero si tiene documento.
# mostrar explicaciones en los otros casos

edad = int (input("Ingrese su edad: "))

if edad >= 18:
    documento = input ("Tiene documento? (si/no): ")
    if documento == "si":
        print ("Usted puede votar")
    else:
        print ("Usted no tiene documento")
        print ("no puede votar")
else:
    print ("Usted no puede votar")
    print ("Porque es menor de edad")