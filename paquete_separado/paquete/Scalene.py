from paquete.Triangle import Triangle
from paquete.Point import Point

class Scalene(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)

    def __str__(self):
        return f"Triángulo Escaleno: {super().__str__()}"