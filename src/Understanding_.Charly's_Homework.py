#Metodo de las Listas: .reverse()
"""
El metodo .reverse() invierte el orden de los elementos en una lista.
Su funcionamiento es permanente, es decir, no se puede volver a la lista original, a menos que se vuelva a
modificar la lista.
No se puede guardar en otra variable, ya que no devuelve ningun valor, solo modifica la lista original.
Es la unica funcion del comando .reverse().
Si se agrega un argumento, el metodo .reverse() no respondera, tronará y marcara error.
"""
name = ['Lalo', 'Charly', 'Anubis', 'Dictador']
print(name)
print('Aplicando modo inverso'.upper())
name.reverse()
print(name)
#Uso de la operacion de Secuencias "slicing" [::x]
"""
El slicing permite obtener una copia de la lista original y modificarla sin afectar la original.
Ordena la lista de una forma secuencial. De acuerdo al valor que se defina en el slicing
Usar slicing con el valor '2', tomara el primer elemento y tomara el siguiente dos terminos despues del primero
Usar slicing con el valor '-2', seria lo mismo pero a la inversa (derecha a izquierda).
EJEMPLO:
"""
print('Extension de lista'.upper())
name = ['Lalo', 'Charly', 'Anubis', 'Dictador', 'Carlos', 'Valentin', 'Fernando', 'Veracruz']   
print(name)
print("Aplicando Slicing".upper())
value = name[::2]
print(value))

#Metodo Built-in sorted()
"""
El metodo sorted() permite ordenar los elementos de un objeto iterable.
Puede modificar la lista original o bien, devolverla ordenada en una nueva variable
EJEMPLO
"""
print('Metodo sorted()'.upper())
numeros = [6, 2, 9, 8, 12, 1]
print(numeros)
numeros = sorted(numeros)
print(numeros)
print('Metodo sorted() inverso'.upper())
numerosos = sorted(numeros, reverse=True)
print(numerosos)

#Metodo sorted() con strings/palabras
print('Metodo sorted() con strings/palabras'.upper())
palabras = ['Lalo', 'Charly', 'Anubis', 'Dictador']
print(palabras)
palabras_ordenadas = sorted(palabras)
print(palabras_ordenadas)
palabrotras_ordenadas = sorted(palabras, reverse=True)
print(palabrotras_ordenadas)

#Metodo len() - Devuelve la cantidad de elementos de una lista
"""
El metodo len() indica la cantidad de elementos que contiene una lista, cadena de texto, tupla, diccionario, etc.
"""
#Numeros
numeros = [6, 2, 9, 8, 12, 1]
print(len(numeros))
#Strings
palabras = ['Lalo', 'Charly', 'Anubis', 'Dictador']
print(len(palabras))

#Statement de lista [0]
"""
Un statement de lista [x] se utiliza para acceder a un elemento de una lista.
"""
#Seleccionar un argumento de una lista
frutas = ['mango', 'durazno', 'fresa', 'melon', 'limon']
print(frutas)
frutas_favoritas = [frutas[3]]
print(frutas_favoritas)

#Modificar un argumento de una lista
frutas = ['mango', 'durazno', 'fresa', 'melon', 'limon']
frutas[3] = 'piña'
print(frutas)