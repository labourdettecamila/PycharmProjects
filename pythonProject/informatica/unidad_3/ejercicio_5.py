estados_unidos = {'Pais': 'Estados Unidos',
                  'Ciudades':["Chicago", "California"],
                  'Idioma':'Inglés',
                  'Moneda':'USD'}

mexico = {'Pais': 'Mexico',
                  'Ciudades':["Guadalajara", "Acapulco"],
                  'Idioma':'Español',
                  'Moneda':'MX'}

alemania = {'Pais': 'Alemania',
                  'Ciudades':["Munich", "Berlín"],
                  'Idioma':'Alemán',
                  'Moneda':'Euro'}

paises_a_visitar = [estados_unidos, mexico, alemania]
ciudades_a_visitar = []

print("Ciudades a visitar:")
for elemento in paises_a_visitar:
    for ciudad in elemento['Ciudades']:
        ciudades_a_visitar.append(ciudad)

print(ciudades_a_visitar)

if "suecia" in paises_a_visitar:
    print("Existe Suecia")
else:
    print("No existe Suecia")

