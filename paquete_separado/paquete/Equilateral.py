import math
from paquete.Point import Point
from paquete.Triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + side, origin.get_y())
        altura = math.sqrt(3) / 2 * side
        p3 = Point(origin.get_x() + side / 2, origin.get_y() + altura)
        super().__init__(p1, p2, p3)

    def compute_inner_angles(self):
        return (60.0, 60.0, 60.0)

    def compute_area(self):
        a, _, _ = self.get_sides()
        return (math.sqrt(3) / 4) * a**2

    def __str__(self):
        return f"Triángulo Equilátero: {super().__str__()}"