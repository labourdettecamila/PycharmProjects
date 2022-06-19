usuario = {'nombre': 'Mark', 'apellido': 'Ronnan', 'dni': '8237123'}
print("\n")
print(usuario)

print("\n")

print(usuario.items())
print("\n")

for key, value in usuario.items():
    if key != "dni":
        print(f"{key.title()}: {value}")
    else:
        print(f"{key.upper()}: {value}")


