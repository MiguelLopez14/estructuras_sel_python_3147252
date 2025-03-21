'''
operadores lógicos

Aquellos que operan unicamente
con valores booleanos (V F)
Acorde a las tablas de verdad
'''
#Ejemplo 1: Operador not:

y = not True
print("El resultado de operar con not es",y)

#Ejemplo 2: Operador and:

y = False and True
print("El resultado de operar con and es",y)

#Ejemplo 3: Operador or:

y = False or True
print("El resultado de operar con or es",y)

'''
Jerarquia de Precedencia de operadores

(Logicos inclusive)
1. ()
2. **
3. *, /, //, %
4. +, -
5. ==, !=, >, >=, <, <=
6. not
7. and
8. or
9. =
'''

#Ejemplo 4: Jerarquia de operadores
y = False and not True or False

print ("El resultado de operar con jerarquia de operacion es" ,y)


#Ejemplo 5: Operadores relacionales y logicos

y = not 3 > 4 and 4 == 4 or 3 < 2
print ("El resultado de operar con relacionales y logicos es", y)

#Ejemplo 6: Operadores Aritmeticos, relacionales y logicos

y = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2
print ("El resultado de operar con aritmeticos, relacionales y logicos es", y)

#Ejemplo 7: con parentesis

y = (3 + 5) * (2 > 3) and 4 == 4 or not 3 < 2
print ("El resultado de operar con parentesis es", y)

#Ejemplo 8: Todo Junto

y = 4 ** 2 * 3 < 6 / (7 - 5) and 7 * 2 + 1 == 14 or not 3 + 5 < 2
print ("El resultado de operar todo junto es", y)


