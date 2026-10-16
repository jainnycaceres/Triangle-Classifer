import math 
from triangle import is_valid_triangle, classify_triangle


def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_zero_side():
    assert is_valid_triangle(0, 4, 5) is False


def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene():
    assert classify_triangle(2, 3, 4) == "Scalene"


def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_triangle_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
