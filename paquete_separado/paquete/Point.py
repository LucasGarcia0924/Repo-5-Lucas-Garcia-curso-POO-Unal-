
class Point:
    definition: str = "Entidad geométrica abstracta que representa una ubicación en un espacio."
    
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x: float):
        self.__x = x

    def set_y(self, y: float):
        self.__y = y

    def move(self, new_x: float, new_y: float) -> None:
        self.set_x(new_x)
        self.set_y(new_y)

    def reset(self) -> None:
        self.__x = 0
        self.__y = 0

    def compute_distance(self, point: "Point") -> float:
        distance = ((self.__x - point.get_x()) ** 2 + (self.__y - point.get_y()) ** 2) ** 0.5
        return distance