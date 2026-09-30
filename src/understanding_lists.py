"""
Las listas permiten almacenar informacion en un lugar, la cantidad que queramos.
Una lista es una coleccion de elementos que tienen un orden especifico. Pueden incluir strings, enteros, floats, nombres, etc.
Son elementos mutables: puede modificarse el tamaño de la lista.
Se recomienda nombrar una variable del tipo lista en plural.

En Python, los corchetes [] indican una lista, sus elemntos se separan por comas.
"""
#Ejemplo
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)

#¿Como podemos acceder a los elementos de una lista?
"""
Las listas son colecciones ordenadas. Se puede acceder a un elemento de una lista 
diciendole a Pytho la posicion o indice del elemento deseado.
Para obtener el valor deseado, se debe escribir el nombrede la lista, seguido del 
indice del elemento entre corchetes.
"""
#bicycles = ['trek', 'cannondale', 'redline']
print(bicycles[0])
print(bicycles[0].upper())

#Los indices comienzan en 0, no en 1. (De izquierda a derecha)
#Los indices comienzan en -1, no en 0. (De derecha a izquierda)
print(bicycles[-1]) #redline

#Utilizando valores individuales de una lista
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)
