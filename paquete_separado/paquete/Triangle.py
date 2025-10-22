import math
from paquete.Shape import Shape
from paquete.Point import Point

class Triangle(Shape):
    
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__update_sides()


    def get_points(self):
        return (self.__p1, self.__p2, self.__p3)

    def set_points(self, p1: Point, p2: Point, p3: Point):
        self.__p1, self.__p2, self.__p3 = p1, p2, p3
        self.__update_sides()

    def get_sides(self):
        return (self.__a, self.__b, self.__c)

    def __update_sides(self):
        self.__a = self.__p2.compute_distance(self.__p3)
        self.__b = self.__p1.compute_distance(self.__p3)
        self.__c = self.__p1.compute_distance(self.__p2)

    def compute_perimeter(self):
        return self.__a + self.__b + self.__c

    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def compute_inner_angles(self):
        A = math.degrees(math.acos((self.__b**2 + self.__c**2 - self.__a**2) / (2 * self.__b * self.__c)))
        B = math.degrees(math.acos((self.__a**2 + self.__c**2 - self.__b**2) / (2 * self.__a * self.__c)))
        C = 180 - (A + B)
        return (A, B, C)

    def __str__(self):
        return (
            f"Triángulo con vértices "
            f"A({self.__p1.get_x()}, {self.__p1.get_y()}), "
            f"B({self.__p2.get_x()}, {self.__p2.get_y()}), "
            f"C({self.__p3.get_x()}, {self.__p3.get_y()})"
        )