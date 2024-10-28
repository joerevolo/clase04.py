#----------------
#circulo
#fecha : 28/10/24
#Autor: Joe Revolo
#----------------
import math #importamo la libreria mathematic
#funciones
def area (r ): #r es el parametro
    xa= math.pi * math.pow(r,2)
    return round(xa,1)
def diametro(r):
    xd = 2 * r
    return round(xd,1)
def circunferencia(r):
    xc = 2 * math.pi * r 
    return round(xc,1)   
#----------------
#bloque principal
#----------------
print('-------')
print('CIRCULO')
print('-------')
xr= int(input('ingrese radio del circulo : \n'))# \n salta una linea 
if (xr > 0):
    print('El area del circulo es: ', area(xr)) #xr es el argumento
    print('El diametro es : ', diametro(xr))
    print('La circunferencia es : ', circunferencia(xr))
else:
    print('Verificar radio ingresado')