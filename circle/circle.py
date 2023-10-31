import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio no puede ser negativo")
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("El radio no puede ser negativo")
        self._radius = radius

    def get_area(self):
        return math.pi * self._radius**2

    def get_perimeter(self):
        return 2 * math.pi * self._radius

    def __mul__(self, radius):
        if radius <= 0:
            raise ValueError("El multiplicador no puede ser negativo")
        return Circle(self._radius * radius)

    def __str__(self):
        return f"Circulo de radio {self._radius}"
