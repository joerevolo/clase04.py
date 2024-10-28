#--------------------
#Trabajando con lista
#fecha : 28/10/24
#Autor: Joe Revolo
#--------------------
import math
n = [10 , 50 , 8 , 600 , 5 ,23]
print('ordena la lista ascendentemente')
n.sort() #ordena la lista ascendete
print(n)

print('ordena la lista descendentemente')
n.sort(reverse=True)#ordena la lista ascendente
print(n)

print('maximo valor de la lista: ' , max(n))
print('minimo valor de la lista: ' , min(n))
print('La suma es: ' , math.fsum(n))
#con pop se debe indicar la posicion del elemento a eliminar
print('elimina un elemento de la lista (pop): ', n.pop(1))
#Con remove se debe indicar el valor a eliminar 
print('elimina un elemento de la lista (remove): ', n.remove(600))
print(n)
#Listar los elementos de la lista 
#xe toma cada elemento de la lista 
print('\n')
for xe in n:
    print(xe) #¿es par?
#! significa not    
for xe in n:
    if (xe % 2 ==0): #¿es impar?
        print(xe)

