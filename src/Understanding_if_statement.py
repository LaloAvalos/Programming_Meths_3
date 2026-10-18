#If Statement
cars = ['audi', 'bmw', 'tsubaru', 'toyota']
for car in cars:
    print(car)
    if car == 'audi':
        print(car.upper())
    else:
        print(car)



# El condicional es el corazion de un if
#Condicional Verdadero - Condicional True
#Condicional == para determinar igualdad

truck = 'ford'
print(truck == 'ford') # True

#Condicional falso
print(truck == "toyota") # False

#Condicional != para dterminar desigualdad

print(truck!="toyota") # True
print(truck!="Ford") # False

print('Condicionales con numeros'.upper())
age = 34
print(age==18) # False

answer = 17
if answer != 42:
    print('Respuesta incorrecta')

print('condiciones utilizando <'.upper())
age = 18
print(age < 18) # False

print('condiciones utilizando <='.upper())
print(age <= 18) #True

print('condiciones utilizando >='.upper())
print(age >= 18) #True

