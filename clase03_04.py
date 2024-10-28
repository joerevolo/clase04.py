#--------------------
#Trabajando con lista
#fecha : 28/10/24
#Autor: Joe Revolo
#--------------------
#Algoritmo es una lista
algoritmos=['KNN', 'KMEANS', 'PCA', 'Random', 'LM']
#Analizar
print('Cantidad de elementos : ' , len(algoritmos))  
print('El primer elemento es : ' , algoritmos[0])
print('El ultimo elemento es : ', algoritmos[len(algoritmos)-1])
#adicionar un elemento a la lista
algoritmos.append('SMV')
print(algoritmos)
#insertar un elemeento en una posicion
algoritmos.insert(1, 'XYY')
print(algoritmos)
#Eliminar un elemento especifico
algoritmos.remove('XYY')
print(algoritmos)