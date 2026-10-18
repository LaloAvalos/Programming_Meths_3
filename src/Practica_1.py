#Crear una lista con los primeros 10 numeros cuadráticos.
squares = [value**2 for value in range(1,11)]
print(squares)

#Metodo Charly
print("Metodo charly".upper())
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

