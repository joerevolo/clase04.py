'''
Boleta
ingresa nombre producto 
                precio
                cantidad
hallar el importe 
condicion: cantidad >10 desciento 15%
total_pagar=cantidad * precio - descuento                
'''
def total_pagar(xpre , xcan):
    impor = xpre * xcan
    if (xcan >10):
        return impor - 0.15*impor
    else:
        return impor
    
xnom = input('ingrese el nombr del producto : ')
xpre = float(input('ingrese el precio del producto: '))
xcan =int(input('ingrese la cantidad de productos'))

#resultado
print('-----------------------------')
print('Boleta N° 001-025120')
print('producto:' , xnom)
print('precio:', xpre) 
print('cantidad', xcan)
print('total pagar :' , total_pagar(xpre,xcan))   