usuarios = ["marmeant", "gruntmar", "tokcie", "ciebank",
            "mueslicie", "sanero", "robedrock", "admin", "derivero","posloth", "claypo", "locustpo", "mostter"]

usuario_ingresado = input("Usuario: ")

if usuario_ingresado in usuarios:
    if usuario_ingresado == "admin":
        print("Bienvenido Administrador, ¿en qué lo puedo ayudar?")
    elif usuario_ingresado == "claypo":
        print(f"Acceso denegado")
    else:
        print (f"Bienvenido estimado {usuario_ingresado.title()}, le deseamos un buen día ")
