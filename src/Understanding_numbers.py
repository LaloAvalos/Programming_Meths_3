#Numeros
#Enteros - Integers
"""
Los numeros enteros los podemos sumar (+), restar (-), multiplicar (*) y dividir (/).
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1 + number_2)

#Enteros
#Sumar +
#Restar -
#Multiplicar *
#Dividir /
#Division entera //
#Potencias **n
print(3**2) # 3^2
print(3**3) # 3^3
print(10**6) # 10^6
print(10%2) # Modulo (mod)
age = 18
print(age)
name = "Lalo Avalos"
print(name, age)

"""
Python llama Floats a cualquier numero con punto decimal

"""
print(0.1 + 0.1)
print(0.2 - 0.2)
print(2*0.1)
print(2*0.2)

#Imprimir la edad de alguien
age = 18 # Variable del tipo int/entera
message = "Lalo tiene" + str(age) + "años"
print(message)

#TypeError
"""
TypeError: Python no puede reconoer e; tipo de informacion que se esta utilizando.
"""
message_f = f"Charly tiene {age} años"
print(message_f)

#Metodo build-in type()
print(type(age))
