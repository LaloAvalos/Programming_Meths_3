#Tuplas
"""
Las tuplas son listas de elementos que no cambian de tamaño.
Las tuplas son listas inmutables

Ejemplo:
Si tenemos un rectangulo que siempre va a tener cierto tamaño, podemos asegurar que sus 
dimensiones no van a cambiar si colocamos sus valores en una tulpa.
"""
dimensions = (500, 1000, 20)
print("tupla re-definida:".upper(), dimensions)

#Tipos de datos booleanos
answer = True
print(answer)

""" print(dir(answer)) """
dimensions = (200, 50)
print(dimensions)

#Como acceder a un elemento de la tupla
print("metodo tupla".upper())
print("El largo de tu rectangulo es: ", dimensions[0])
print("El ancho de tu rectangulo es: ", dimensions[1])

print(f"El largo de tu rectangulo es: {dimensions[0]}")
print(f"El ancho de tu rectangulo es: {dimensions[1]}")

#Looping through a tuple
for dimension in dimensions:
    print(dimension)

names = ["montes", 'charly', 'isidro', 'lalo', 'miguel']
print(names)

#Cambiar argumento de una lista
names[0] = 'angel'
print(names)

#Truco de Charly
""" Cambiar argumentos en una tupla"""
dimensions = (1000, 5000, 2000)
print('Truco Charly'.upper())
print(dimensions)

#Booleano

answer = True
print(answer)
answer = False
print(answer)