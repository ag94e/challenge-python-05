import math


def square_area(side):
    """Returns the area of a square"""
    return float(side**2)


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return float(base * height)


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return float((base * height) / 2)


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return float((diagonal_1 * diagonal_2) / 2)


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return float(((base_minor + base_major) / 2) * height)


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return float((perimeter * apothem) / 2)


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round(math.pi * (radius**2), 5)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            """Values for tests on each areas"""
            self.sqr = {9: 3, 49: 7}
            self.rec = {10: [2, 5], 15: [5, 3]}
            self.tri = {5: [2, 5], 20: [10, 4]}
            self.rom = {16: [8, 4], 15: [10, 3]}
            self.trap = {40: [5, 11, 5], 16: [5, 3, 4]}
            self.poly = {5: [5, 2], 15: [5, 6]}
            self.circ = {78.53982: 5, 38.48451: 3.5}


        def test_square_area(self):
            for key, val in self.sqr.items():
                self.assertEqual(key, square_area(val))


        def test_rectangle_area(self):
            for key, val in self.rec.items():
                self.assertEqual(key, rectangle_area(val[0], val[1]))


        def test_triangle_area(self):
            for key, val in self.tri.items():
                self.assertEqual(key, triangle_area(val[0], val[1]))
        
        
        def test_rhombus_area(self):
            for key, val in self.rom.items():
                self.assertEqual(key, rhombus_area(val[0], val[1]))
        
        
        def test_trapezoid_area(self):
            for key, val in self.trap.items():
                self.assertEqual(key, trapezoid_area(val[0], val[1], val[2]))
        
        
        def test_regular_polygon_area(self):
            for key, val in self.poly.items():
                self.assertEqual(key, regular_polygon_area(val[0], val[1]))
        
        
        def test_circumference_area(self):
            for key, val in self.circ.items():
                self.assertEqual(key, circumference_area(val))
        
        
        def tearDown(self):
            del(self.sqr)
            del(self.rec)
            del(self.tri)
            del(self.rom)
            del(self.trap)
            del(self.poly)
            del(self.circ)

    unittest.main()
