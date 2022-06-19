active = True
orders = []

while active:
    print("\n")
    print("Farmacia - Opciones")
    print("\t(1)Agregar")
    print("\t(2)Listar")
    print("\t(3)Salir")

    option = input("Opción: ")

    if option == "3":
        active = False

    elif option == "1":


        item = {}

        medicamento = input("Nombre del medicamento: ")
        laboratorio = input("Nombre del laboratorio: ")
        cantidad = input("Cantidad: ")

        item['medicamento'] = medicamento
        item['laboratorio'] = laboratorio
        item['cantidad'] = cantidad

        if item in orders:
            print(f"Medicamento existente")
        else:
            orders.append(item)

    elif option == "2":
        print(f"Órdenes: {orders}")

    else:
        print(f"La opción {option} no es válida")