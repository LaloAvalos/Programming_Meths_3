players = ["Jason", "Benjamin", "Bryan", "Shecid", "Allizon", "Wendy"]
print("Lista Original:", players)

#SLICING

print("Slicing".upper())
print(players[3:6])

"""
El slicing permite trabajar con un grupo especifico de una lista: al resultado se le conoce
como un "slice".
Ejemplo:
players = ["Jason", "Benjamin", "Bryan", "Shecid", "Allizon", "Wendy"]
"""
print("Ejemplos de slicing".upper()) 
print("1:4", players[1:4]) # [1, 4) -> [Benjamin, Bryan, Shecid]
print(":3", players[:3]) # [0, 3) -> [Jason, Benjamin, Bryan]
print("2:5", players[2:5]) # [2, 5) -> [Bryan, Shecid, Allizon]
print("(-3:)", players[-3:]) # [3, 6) -> [Shecid, Allizon, Wendy]

#CASOS ESPECIALES DEL SLICING

#players = ["Jason", "Benjamin", "Bryan", "Shecid", "Allizon", "Wendy"]

print("casos especiales del slicing".upper())
print(players)
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[:0])
print(players[0:1])

#Looping throught a slice
print("Looping through a slice".upper())
students = ["Jason", "Benjamin", "Bryan", "Shecid", "Allizon", "Wendy"]

#Slicing [::] Tarea
for student in students[3:5]:
    print(f"El estudiante {student}, va a pasar la materia")

# ¿Como podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food

#MANERAS DE COPIAR UNA LISTA

#Metodo 1. Utilizando slicing
my_friend_food_2 = my_food[:]

#Metodo 2. Utilizando el metodo de las listas copy()
my_friend_food_3 = my_food.copy()

#Metodo 3. Utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)

