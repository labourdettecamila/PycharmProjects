clientes = ["ernesto", "martin andrés", "sofía", "lucía", "jose maría", "andrés"]

clientes_title = []

for cliente in clientes:
    clientes_title.append(cliente.title())
print(clientes_title)


# si quiero crear una copia de la lista (cosa que si la modifico, pueda tener guardada la original):

clientes_copia = clientes_title[:]


clientes_copia.append("Martina")
clientes_copia.append("Josefina Isabel")
clientes_copia.append("Tomás")

print(clientes_copia)

# si quiero que el elemento se agregue al principio y no al final, primero invierto la lista, lo agrego y la vuelvo a invertir
# list.reverse ()
# otra forma: list.insert (posición, elemento)

# otra forma

nuevos_huespedes = ["Martina", "Josefina Isabel", "Tomás"]

lista_nueva = clientes + nuevos_huespedes

print(lista_nueva)

# para eliminar el último elemento

lista_nueva.pop()

print(lista_nueva)