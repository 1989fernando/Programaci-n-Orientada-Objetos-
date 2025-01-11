"""
Programa: Conversión de Temperaturas
Funcionalidad:
Este programa convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
El usuario puede elegir la dirección de conversión (Celsius a Fahrenheit, Fahrenheit a Kelvin, etc.)
e ingresar el valor que desea convertir. El programa utiliza diferentes tipos de datos
como integer, float, string y boolean para realizar las operaciones y mostrar los resultados.
"""

def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    :param celsius: Temperatura en grados Celsius (float o int)
    :return: Temperatura en grados Fahrenheit (float)
    """
    return (celsius * 9/5) + 32


def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte temperatura de Fahrenheit a Celsius.
    Fórmula: C = (F - 32) * 5/9
    :param fahrenheit: Temperatura en grados Fahrenheit (float o int)
    :return: Temperatura en grados Celsius (float)
    """
    return (fahrenheit - 32) * 5/9


def celsius_a_kelvin(celsius):
    """
    Convierte temperatura de Celsius a Kelvin.
    Fórmula: K = C + 273.15
    :param celsius: Temperatura en grados Celsius (float o int)
    :return: Temperatura en Kelvin (float)
    """
    return celsius + 273.15


def kelvin_a_celsius(kelvin):
    """
    Convierte temperatura de Kelvin a Celsius.
    Fórmula: C = K - 273.15
    :param kelvin: Temperatura en Kelvin (float o int)
    :return: Temperatura en grados Celsius (float)
    """
    return kelvin - 273.15


def main():
    """
    Programa principal que interactúa con el usuario.
    Permite seleccionar la conversión deseada y realiza la operación.
    """
    print("Bienvenido al programa de conversión de temperaturas.\n")
    print("Opciones de conversión:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")

    # Entrada del usuario: selección de opción y valor
    opcion = int(input("\nSeleccione una opción (1-4): "))
    if opcion not in [1, 2, 3, 4]:
        print("Opción inválida. Intente nuevamente.")