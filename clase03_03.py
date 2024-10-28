#----------------
#circulo
#fecha : 28/10/24
#Autor: Joe Revolo
#----------------
import math #importamo la libreria mathematic
#funciones
def area (r , d): #r es el parametro
    xa= math.pi * math.pow(r,2)
    return round(xa,d)
def diametro(r , d):
    xd = 2 * r
    return round(xd,d)
def circunferencia(r, d):
    xc = 2 * math.pi * r 
    return round(xc,d)   
#----------------
#bloque principal
#----------------
print('-------')
print('CIRCULO')
print('-------')
try:
    xr= int(input('ingrese radio del circulo : \n'))# \n salta una linea 
    xdec = int(input('Ingrese numero decimal : \n'))
    if (xr > 0 and xdec >= 0):
        print('El area del circulo es: ', area(xr,xdec)) #xr es el argumento
        print('El diametro es : ', diametro(xr,xdec))
        print('La circunferencia es : ', circunferencia(xr,xdec))
    else:
        print('Verificar radio ingresado y numeros decimales ingresados')
except:
    print('error de data . . . verificar')