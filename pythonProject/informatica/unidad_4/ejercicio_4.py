active = True
archivos = []

while active:
    print("\n")
    print("Seleccione una opción")
    print("\t(1)Lavandería")
    print("\t(2)Recepción")

    option = input("Opción: ")


    if option == "1":

        ticket = {}

        habitacion = input("Número de habitación: ")
        prendas = input("Cantidad de prendas: ")
        fecha = input("Fecha del servicio: ")

        ticket['habitacion'] = habitacion
        ticket['prendas'] = prendas
        ticket['fecha'] = fecha

        archivos.append(ticket)

    elif option == "2":
        habitacion_buscada = input("Número de habitación: ")
        total_prendas = []
        total_prendas_int = 0

        for archivo in archivos:
            if archivo['habitacion'] == habitacion_buscada:
                total_prendas.append(archivo['prendas'])

        for element in total_prendas:
            total_prendas_int = total_prendas_int + int(element)

        print(f"El total de prendas es {total_prendas_int}. Son {total_prendas_int*3} pesos.")

        if total_prendas_int != 0:
            print("Seleccione un estado:")
            print("\t(1)Pagado")
            print("\t(2)En deuda")

            estado = input("Opción: ")

            if estado == "1":
                for archivo in archivos:
                    if archivo['habitacion'] == habitacion_buscada:
                        archivos.remove(archivo)



