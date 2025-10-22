import math
from paquete.Triangle import Triangle
from paquete.Point import Point

class Isosceles(Triangle):
    def __init__(self, base: float, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + base, origin.get_y())
        altura = math.sqrt(side**2 - (base / 2)**2)
        p3 = Point(origin.get_x() + base / 2, origin.get_y() + altura)
        super().__init__(p1, p2, p3)

    def __str__(self):
        return f"Triángulo Isósceles: {super().__str__()}"