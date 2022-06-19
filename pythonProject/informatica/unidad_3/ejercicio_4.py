encuesta = {'anonimo1': '6',
               'anonimo2': '9',
               'anonimo3': '5',
               'anonimo4': 'x',
               'anonimo5': 'x',
               'anonimo6': '8',
               'anonimo7': '3',
               'anonimo8': '10',
               'anonimo9': '4',
               'anonimo10': '5',
               'anonimo11': 'x',
               'anonimo12': '2',
               'anonimo13': '7',
               'anonimo14': '5',
               'anonimo15': '2',
               'anonimo16': '8',
               'anonimo17': '10'}

encuesta_limpia = {}


contador = 0
for clave, valor in encuesta.items():
    if valor == "x":
        contador += 1
    else:
        encuesta_limpia[clave] = valor
print("Empleados que no contestaron:", contador)
print("Empleados que contestaron:", len(encuesta_limpia))

suma_puntajes = 0
for value in encuesta_limpia.values():
    suma_puntajes += int(value)
print("Suma de puntajes:", suma_puntajes)

# averiguar cómo calculo el porcentaje de aceptación


