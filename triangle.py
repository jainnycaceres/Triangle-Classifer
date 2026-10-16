import math

def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if math.isclose(a * a + b * b, c * c, rel_tol=1e-9, abs_tol=1e-9):
        right = True
    elif math.isclose(a * a + c * c, b * b, rel_tol=1e-9, abs_tol=1e-9):
        right = True
    elif math.isclose(b * b + c * c, a * a, rel_tol=1e-9, abs_tol=1e-9):
        right = True
    else:
        right = False

    if a == b == c:
        shape = "Equilateral"
    elif a == b or a == c or b == c:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    if right:
        return "Right " + shape

    return shape






