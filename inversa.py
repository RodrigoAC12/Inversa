"""
Módulo que calcula el inverso de un número y maneja excepciones personalizadas.
"""

class ExceptionNumeroCero(Exception):
    """Excepción personalizada para números iguales a cero."""

try:
    x = float(input("Número: "))
    if x == 0:
        raise ExceptionNumeroCero
    inversa = 1 / x
    print(f"Número = {x}, su inverso es: {inversa}")
except ValueError:
    print("Debe ser un int o float")
except ZeroDivisionError:
    print("Infinito, el valor tiene que ser diferente a 0")
except ExceptionNumeroCero:
    print("No se permite el número cero")
finally:
    print("Final de la aplicación")
