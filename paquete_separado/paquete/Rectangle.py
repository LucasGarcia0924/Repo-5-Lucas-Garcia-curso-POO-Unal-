from paquete.Shape import Shape
from paquete.Point import Point
from paquete.Line import Line

class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__()
        method = kwargs.get("method", "1")
        if method == "1":
            corner: Point = kwargs.get("corner", Point())
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)
            self.__center = Point((corner.get_x() + self.__width) / 2, (corner.get_y() + self.__height) / 2)
        elif method == "2":
            center: Point = kwargs.get("center", Point())
            self.__center = center
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)
        elif method == "3":
            corner1: Point = kwargs.get("corner1", Point())
            corner2: Point = kwargs.get("corner2", Point())
            self.__width = abs(corner2.get_x() - corner1.get_x())
            self.__height = abs(corner2.get_y() - corner1.get_y())
            self.__center = Point((corner1.get_x() + corner2.get_x()) / 2, (corner1.get_y() + corner2.get_y()) / 2)
        else:
            lines: list = kwargs.get("lines", [])
            self.__width = lines[0].get_length()
            self.__height = lines[1].get_length()
            self.__center = Point(
                (lines[0].get_start().get_x() + lines[0].get_end().get_x()) / 2,
                (lines[0].get_start().get_y() + lines[1].get_end().get_y()) / 2
            )

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_center(self):
        return self.__center

    def set_width(self, width: float):
        self.__width = width

    def set_height(self, height: float):
        self.__height = height

    def set_center(self, center: Point):
        self.__center = center

    def compute_area(self) -> float:
        return self.__width * self.__height

    def compute_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def compute_interference_point(self, point: Point) -> bool:
        left = self.__center.get_x() - self.__width / 2
        right = self.__center.get_x() + self.__width / 2
        bottom = self.__center.get_y() - self.__height / 2
        top = self.__center.get_y() + self.__height / 2
        if left <= point.get_x() <= right and bottom <= point.get_y() <= top:
            print(f"El punto ({point.get_x()}, {point.get_y()}) está dentro del rectángulo.")
            return True
        else:
            print(f"El punto ({point.get_x()}, {point.get_y()}) está fuera del rectángulo.")
            return False

    def compute_interference_line(self, line: "Line") -> None:
        if self.compute_interference_point(line.get_start()) and self.compute_interference_point(line.get_end()):
            print("La línea está completamente dentro del rectángulo.")
        elif self.compute_interference_point(line.get_start()) or self.compute_interference_point(line.get_end()):
            print("La línea intersecta el rectángulo.")
        else:
            print("La línea está completamente fuera del rectángulo.")

    def __str__(self) -> str:
        return f"Rectángulo centrado en ({self.__center.get_x()}, {self.__center.get_y()}) con ancho {self.__width} y alto {self.__height}."