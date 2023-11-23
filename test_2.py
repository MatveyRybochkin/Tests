import unittest
from main_2 import Square

class TestSquare(unittest.TestCase):

    def test_calculate_perimeter(self):
        square = Square(5)
        self.assertEqual(square.calculate_perimeter(), 20)
        
        
    def test_2_calculate_perimeter(self):
        square = Square(10)
        self.assertEqual(square.calculate_perimeter(), 40)

    def test_calculate_area(self):
        square = Square(5)
        self.assertEqual(square.calculate_area(), 25)
        
    def test_2_calculate_area(self):
        square = Square(10)
        self.assertEqual(square.calculate_area(), 100)

if __name__ == '__main__':
    unittest.main()