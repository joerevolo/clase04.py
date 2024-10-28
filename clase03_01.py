#funciones matematicas

import math
print('P1 : ', math.pi)
xn = 144 
print('El tipo de dato de exn es : ', type(xn))
print('raiz cuadrada : ', math.sqrt(xn))
#potencia 
print('xn elevado al cubo: ', math.pow(xn,3))

xd=14.568
print('Redondeo hacia arriba CIELO: ', math.ceil(xd))
print('Redondeo hacia arriba PISO' , math.floor(xd))
print('Redondeo a un decimal' , round(xd , 1))

#factorial
print('El factorial del numero 4 : ', math.factorial(4))
#Muestra el valor del nmero irracional
#tiene infinitos numeros decimales al igual que pi
print('Valor de e: ', math.e)
#Recordar 
print('La division entera de 17 /3 :', (17//3))
#obtener la parte entera de un numero
print('Truncar un numero: ',math.trunc(78.89))
num = [10.30, 5.89, 9, 20]
#fsum es una funcion que suma una lista de numeros
print('La suma de lista: ', math.fsum(num))
print('La suma de lista truncada',math.trunc(math.fsum(num)))


#% --> halla el  resiudo
#%--> operador modulo 
print('El residuo de 7%2: ', (7%2))
print('El residuo de -7%2: ', math.fmod(7,2))