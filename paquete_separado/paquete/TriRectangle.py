import math
from paquete.Triangle import Triangle
from paquete.Point import Point

class TriRectangle(Triangle):
    def __init__(self, base: float, height: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + base, origin.get_y())
        p3 = Point(origin.get_x(), origin.get_y() + height)
        super().__init__(p1, p2, p3)

    def compute_area(self):
        a, b, c = self.get_sides()
        return (a * b) / 2

    def __str__(self):
        return f"Triángulo Rectángulo: {super().__str__()}"