class Ballena:
    def __init__(self, nombre, edad, sexo, peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso

willy = Ballena('Willy', 9, 'M', 2000)

print(f"Mi ballena es {willy.nombre}")

def estado(self):
    return f"Estado de la ballena:" \
           f"\n\tNombre: {self.nombre}" \
           f"\n\tEdad: {self.edad}" \
           f"\n\tSexo: {self.sexo}" \
           f"\n\tPeso: {self.peso}" \

print(estado(willy))

def nadar(self):
    return f"{self.nombre} está nadando"

print(nadar(willy))



jully = Ballena('Jully', 6, 'F', 1800)
print(f"{jully.nombre} es otra ballena")

def atacar(self):
    return f"{self.nombre} está siendo atacada"

print(atacar(willy))

