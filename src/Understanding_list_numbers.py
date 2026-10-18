#Aun no trabajaremos con listas
"""
Las listas tambien pueden almacenar numeros.
El metodo range() nos ayuda a crear facilmente series de numeros.
Ejemplo
"""
#Metodo build-in range()
"""
El metodo range() nos ayuda a crear facilemnte series de numeros.
El motodo puede incluir o no los limites dependiendo la manera de agruparlos: con parentesis (()) o llaves ([]).
Ejemplo:
for value in range(1,5):
    print(value)
#1
#2
#3
#4
"""
first_ten_numbers = range(0,10)
for value in first_ten_numbers:
    print(value)

#Crear una lista de numeros utilizando range
numbers = list(range(0,10))
print(numbers)

#Lista de numeros pares
even_numbers = list(range(0,10,2))

#Lista de numeros impares
odd_numbers = list(range(1,10,2))
print(odd_numbers)
table_of_Seven = list(range(7,71,7))
print(table_of_Seven)