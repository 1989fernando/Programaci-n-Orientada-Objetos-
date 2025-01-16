# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca  # Atributo publico
        self.modelo = modelo  # Atributo publico
        self.__anio = anio  # Atributo privado (encapsulado)

    def descripcion(self):
        return f"{self.marca} {self.modelo}, {self.__anio}"

    def get_anio(self):
        """Método para acceder al atributo privado __anio"""
        return self.__anio

    def set_anio(self, nuevo_anio):
        """Método para modificar el atributo privado __anio"""
        if nuevo_anio > 1885:  # Validación básica para asegurarse de que es un año razonable
            self.__anio = nuevo_anio
        else:
            print("Año no válido.")

# Clase derivada: Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def descripcion(self):
        """Método sobrescrito para incluir el número de puertas."""
        return f"{super().descripcion()} con {self.puertas} puertas."

# Clase derivada: Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def descripcion(self):
        """Método sobrescrito para incluir el tipo de motocicleta."""
        return f"{super().descripcion()} de tipo {self.tipo}."

# Ejemplo de polimorfismo
vehiculos = [
    Automovil("Toyota", "Corolla", 2020, 4),
    Motocicleta("Harley-Davidson", "Street 750", 2019, "Cruiser"),
    Vehiculo("Ford", "Model T", 1908)
]

for vehiculo in vehiculos:
    print(vehiculo.descripcion())

# Uso de encapsulación
carro = Automovil("Honda", "Civic", 2018, 4)
print("Año original:", carro.get_anio())
carro.set_anio(2022)
print("Año modificado:", carro.get_anio())
