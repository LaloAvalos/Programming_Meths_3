"""
Una list comprenhension (comprension de listas) es una manera concisa de crear listas.
Combina el for, loop y la creacion de nuevos elementos en una sola linea y automaticamente agrega cada elemento 
a la lista, es decir, sin utilizar el metodo append.
"""
squares = [value**2 for value in range(1,11)]
print(squares)
students = ["montes", "David", "El de las Flautas", "El Dictador", "Dante"]
print("Lista Original", students)
students_email = [student+"@upv.edu.mx" for student in students]
print("list comprenhesion", students_email)
