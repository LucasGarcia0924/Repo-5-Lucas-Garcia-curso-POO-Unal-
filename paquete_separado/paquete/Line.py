from paquete.Point import Point

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.__start = start
        self.__end = end
        self.__length = self.compute_length()
        self.__slope = self.compute_slope()

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_length(self):
        return self.__length

    def get_slope(self):
        return self.__slope

    def set_start(self, start: Point):
        self.__start = start
        self.__length = self.compute_length()

    def set_end(self, end: Point):
        self.__end = end
        self.__length = self.compute_length()

    def compute_length(self) -> float:
        return self.__start.compute_distance(self.__end)

    def compute_slope(self) -> float:
        if self.__end.get_x() - self.__start.get_x() == 0:
            return float("inf")  # Pendiente infinita
        return (self.__end.get_y() - self.__start.get_y()) / (self.__end.get_x() - self.__start.get_x())

    def compute_horizontal_cross(self) -> float:
        if self.__slope == 0:
            return float("inf")  # Línea horizontal
        return self.__start.get_y() - self.__slope * self.__start.get_x()

    def compute_vertical_cross(self) -> float:
        if self.__slope == float("inf"):
            return float("inf")
        return self.__start.get_x() - (self.__start.get_y() / self.__slope)

    def __str__(self) -> str:
        return f"Línea desde ({self.__start.get_x()}, {self.__start.get_y()}) hasta ({self.__end.get_x()}, {self.__end.get_y()})"