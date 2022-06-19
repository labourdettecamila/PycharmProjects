class Lampara:
    def __init__(self, fabricante, codigo_fabricante, modelo, amperaje, potencia, diametro, eficiencia_energetica, precio):
        self.fabricante = fabricante
        self.codigo_fabricante = codigo_fabricante
        self.modelo = modelo
        self.amperaje = amperaje
        self.potencia = potencia
        self.diametro = diametro
        self.eficiencia_energetica = eficiencia_energetica
        self.precio = precio

class NPN923:
    def __init__(self, fabricante, codigo_fabricante, modelo, amperaje, potencia, diametro, eficiencia_energetica,
                 precio, codigo_certificado):
        super().__init__(fabricante, codigo_fabricante, modelo, amperaje, potencia, diametro, eficiencia_energetica, precio)
        self.codigo_certificado = codigo_certificado
