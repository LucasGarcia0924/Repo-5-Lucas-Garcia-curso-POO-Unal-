
class Shape:
    def __init__(self):
        self.__is_regular = False

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, is_regular: bool):
        self.__is_regular = is_regular

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_perimeter(self):
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")