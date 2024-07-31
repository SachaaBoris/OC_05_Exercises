class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def calculate_area(self):
        return self.width * self.length

    @property
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area)
print("Périmètre:", rectangle.calculate_perimeter)
