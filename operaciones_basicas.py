"""
Módulo que realiza operaciones básicas.
"""


class Calculadora:
    """
    Clase que realiza operaciones matemáticas básicas.
    """

    def __init__(self):
        self._resultado = 0

    @property
    def resultado(self):
        """Getter para obtener el resultado."""
        return self._resultado

    @resultado.setter
    def resultado(self, valor):
        """Setter para establecer el resultado."""
        self._resultado = valor

    def suma(self, a, b):
        """Devuelve la suma de dos números."""
        self.resultado = a + b
        return self.resultado

    def resta(self, a, b):
        """Devuelve la resta de dos números."""
        self.resultado = a - b
        return self.resultado


class Estadistica:
    """
    Clase que realiza cálculos estadísticos.
    """

    def __init__(self):
        self._datos = []

    @property
    def datos(self):
        """Getter para obtener la lista de datos."""
        return self._datos

    @datos.setter
    def datos(self, valores):
        """Setter para establecer la lista de datos."""
        if isinstance(valores, list):
            self._datos = valores
        else:
            raise ValueError("Los datos deben ser una lista.")

    def promedio(self, numeros):
        """Calcula el promedio de una lista de números."""
        return sum(numeros) / len(numeros) if numeros else 0

    def mediana(self, numeros):
        """Calcula la mediana de una lista de números."""
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        if n == 0:
            return 0
        if n % 2 == 1:
            return numeros_ordenados[n // 2]
        return (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2


def calcular_promedio(numeros):
    """Función independiente para calcular el promedio de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0
