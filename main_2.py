class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2


square = Square(5)
perimeter = square.calculate_perimeter()
area = square.calculate_area()

print(f"Периметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")
