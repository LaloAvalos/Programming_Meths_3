motorcycles = ['honda',"mortalica", 'yamaha',]
print(motorcycles)

#Metodo .append() - Agregar elementos a una lista. (Al final de la lista).
motorcycles.append('kawasaki')
print(motorcycles)

motorcycles_2 = [] #Lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle) # 1er Elemento
motorcycles_2.append("yamaha") # 2do Elemento
motorcycles_2.append("suzuki") # 3er Elemento
print(motorcycles_2)

#Metodo .insert() - Agregar elementos a una lista. (En una posicion especifica de la lista).
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
print("\Lista Original")
print(motorcycles_3)
motorcycles_3.insert(-2, 'ducati')
print("Lista despues del metodo insert")
print(motorcycles_3)

#Metodo .pop() Elimina el ultimo elemento de la lista, pero permite utilizar el elemento despues 
#de eliminarlo.
print("\n\tAqui aprendi a utilizar el metodo pop".upper())
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop() 
print(f"Tu motocicleta borrada es: {deleted_motorcycle.title()}")
print(motorcycles_4)

#Se puede utilizar tambien para eliminar un elemento especifico
print('Eliminar por Indice')
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
print(motorcycle_5)
motorcycles_5.pop(0)
print(motorcycles_5)

#Metodo .remove(), permite eliminar elementos por su valor()


#Ordenar Listas
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() #Ordenar la lista de manera permanente

#Argumento opcional de sort(reverse=True)
print(cars)
