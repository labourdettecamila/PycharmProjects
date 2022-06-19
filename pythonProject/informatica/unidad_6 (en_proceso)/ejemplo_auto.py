class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def car_description(self):
        print(f"Car brand: {self.brand}, Model: {self.model}")

# car_description es un método, es decir, una función dentro de una clase.

bmw = Car("BMW", "X6")
bmw.car_description()

# si quiero llamar a un atributo:

print(f"Marca del vehículo: {bmw.brand}")

# CLASE HIJA:

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

# ElectricCar es hijo de Car

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        # super se usa para heredar los atributos de la superclass (clase padre)
        self.battery = Battery(300)
    def read_battery(self):
        print(f"Battery capacity: {self.battery}")
# recordar que read_battery es un método


