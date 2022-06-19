animals_lista = ["mono", "gato", "perro"]
animals_tupla = ("mono", "gato", "perro")
animals_conjunto = {"mono", "gato", "perro"}
# a los conjuntos se los suele llamar set
animals_dic = {'uno': 'mono', 'dos': 'gato', 'tres': 'perro'}
# recordar que las claves de los diccionarios son únicas

print(animals_lista)
print(animals_tupla)
print(animals_conjunto)
print(animals_dic)

print("\n")

print(type(animals_lista))
print(type(animals_tupla))
print(type(animals_conjunto))
print(type(animals_dic))

print("\n")

animals_lista.append("python")
print(animals_lista)

# no puedo modificar una tupla

animals_conjunto.add("python")
print(animals_conjunto)
# se agrega en cualquier lado porque los conjuntos son desordenados
# si lo intento volver a agregar no hace nada porque no admite elementos repetidos

animals_dic['cuatro']:"python"
print(animals_dic)
# ¿por qué no me anda?


