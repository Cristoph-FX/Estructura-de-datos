import numpy as np


#creacion de lsitas
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
print(lista[6])

lista_vacia=[]
lista_vacia.append(1)
print(lista_vacia)

lista_vacia.append("hola")
print(lista_vacia)
#insetar un boleano en medio de la lista

lista_vacia.insert(1, True)
print(lista_vacia)
print(f"ultimo elemento de la lista es: {lista_vacia[-1]}")

print(f"cuantos elementos tiene la listae: {lista_vacia}")

lista_vacia.remove(1)   

lista_vacia.pop()
print(lista_vacia)

lista_vacia[0]="Modificado"
print("Lista moficada: ",lista_vacia)

lista_vacia.extend([1,2,3])
print("Lista extendida:", lista_vacia)

lista_de_listas=([1,2,3],[4,5,6],[7,8,9])
print("Lista de lista:", lista_de_listas)


print("Elemento de la lista:", lista_de_listas[1][2])

import random
lista_aleatoria=[random.randint(1,100) for _ in range(10)]
print("Lista aleatoria:", lista_aleatoria)

lista_numpy=np.random.randint(1,100,size=10).tolist()
print("Lista numpy aleatoria:", lista_numpy)

lista_numpy.sort()
print("Lista numpy ordenada:", lista_numpy)

lista_numpy.reverse()
print("Lista numpy invertida:", lista_numpy)

print("Buscar elemento en la lista numpy:", 2 in lista_numpy)
print("Buscar elemento en la lista vacia:", 2 in lista_vacia)
print("Buscar elemento en la lista numpy:", lista_numpy.count(50))

lista_copiada=lista_numpy.copy()
print("Lista copiada:", lista_copiada)

lista_copiada= lista_numpy[:]
print("Lista copiada num:", lista_copiada)

lista_numpy.clear()
print("Lista numpy limpia:", lista_numpy)

lista_concatenada=lista_vacia+lista_copiada
print("Lista concatenada:", lista_concatenada)

print("Mayor valor de la lista copiada:", max(lista_copiada))

print("tamaño de la lista copiada:", len(lista_copiada))