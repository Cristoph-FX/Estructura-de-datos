#Las tuplas no se pueden modificar despues de creadas

"""Las tuplas se crean con parentesis y son inmutables, lo que significa
    que no se pueden cambiar una vez creadas(No se usan [])."""

tupla=(1,2,3,4,5,6,7,8,9,10)
print("tupla:", tupla)

print("Longitud de la tupla:", len(tupla))

print("Primer elemento de la tupla:", tupla[0])

print("Ultimo elemento de la tupla:", tupla[-1])

print("Buscar elemento en la tupla:", 3 in tupla)

print("Buscar elemento en la tupla:", tupla.index(3))