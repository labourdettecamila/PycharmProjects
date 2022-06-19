class Esfera:
    def __init__(self, radio):
        self.nombre = "Esfera"
        self.radio = radio
    def nombre(self):
        return self.nombre
    def radio(self):
        return self.radio
    def propiedades(self):
        return f"{self.nombre}, radio: {self.radio}"
    def print_3d(self):
        return f"Imprimiendo {self.nombre}, por favor espere."



class Cubo:
    def  __init__(self, lado):
        self.nombre = "Cubo"
        self.lado = lado
    def nombre(self):
        return self.nombre
    def lado(self):
        return self.lado
    def propiedades(self):
        return f"{self.nombre}, lados: {self.lado}"
    def print_3d(self):
        return f"Imprimiendo {self.nombre}, por favor espere."
    def shape_preview(self):
        return "[][][][] \n[]    [] \n[][][][]"


class PrismaRectangular:
    def __init__(self, base, altura, profundidad):
        self.nombre = "Prisma Rectángular"
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    def nombre(self):
        return self.nombre
    def caracteristicas(self):
        caracteristicas = []
        caracteristicas.append(self.base)
        caracteristicas.append(self.altura)
        caracteristicas.append(self.profundidad)
        return caracteristicas
    def propiedades(self):
        return f"{self.nombre}, base: {self.base}, altura:{self.altura}, profundidad: {self.profundidad}"
    def print_3d(self):
        return f"Imprimiendo {self.nombre}, por favor espere."
    def shape_preview(self):
        return "[][][][][][][][] \n[]            [] \n[][][][][][][][]"