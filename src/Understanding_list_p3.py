#Trabajando con listas

magicians = ['harry', 'ron', 'hermione', 'snape', 'dumbledore']
print(magicians)

print('Imprimir a la mala'.upper())
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])

#Recorrer una lista con un ciclo for
#magicians = ['harry', 'ron', 'hermione', 'snape', 'dumbledore']
print('Imprimir un for')
for magician in magicians:
    print(f"{magician.title()}"," ")
print()

# A esto se le conoce como looping
#for cat in cats:
#for dog in dogs:
#for item in items:

#Identacion 
"""
Python utiliza la identacion para determinar cuando una linea de codigo esta conectada a la linea de codigo anterior.
Basicamente, se utiliza 4 espacios en blanco para escribir el codigo ordenadamente
"""
#No olvidar identar - Tracebacj IdentationErorr
#magicians = ["alice", "david", "carolina"
