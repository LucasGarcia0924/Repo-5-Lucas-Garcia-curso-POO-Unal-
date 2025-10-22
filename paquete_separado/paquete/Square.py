from paquete.Point import Point
from paquete.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float = 1, center: Point | None = None):
        if center is None:
            center = Point()
        super().__init__(method="2", width=side, height=side, center=center)

    def __str__(self) -> str:
        return f"Cuadrado centrado en ({self.get_center().get_x()}, {self.get_center().get_y()}) con lado {self.get_width()}."