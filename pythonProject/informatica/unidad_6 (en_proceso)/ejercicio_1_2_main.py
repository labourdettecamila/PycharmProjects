from ejercicio_1_shapes import Esfera, Cubo, PrismaRectangular

def user_menu():
    print("¿Qué quiere imprimir?")
    print("(1) - Esfera")
    print("(2) - Cubo")
    print("(3) - Prisma Rectangular")

user_menu()

print("\n")
option = input("Opción:")

if option == "1":
    radio = input("Radio en cm: ")
    esfera = Esfera(radio)
    print("\n")
    print(esfera.print_3d())
    print(esfera.propiedades())

elif option == "2":
    lado = input("Lados en cm: ")
    cubo = Cubo(lado)
    print("\n")
    print(cubo.print_3d())
    print(cubo.propiedades())
    print(cubo.shape_preview())

elif option == "3":
    base = input("Base en cm: ")
    altura = input("Altura en cm: ")
    profundidad = input("Profundidad en cm: ")
    prisma_rectangular = PrismaRectangular(base, altura, profundidad)
    print("\n")
    print(prisma_rectangular.print_3d())
    print(prisma_rectangular.propiedades())
    print(prisma_rectangular.shape_preview())