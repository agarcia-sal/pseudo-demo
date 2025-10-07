from math import sqrt

def triangle_area(a: float, b: float, c: float) -> float:
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    semi_perimeter = (a + b + c) / 2
    area = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    area = round(area, 2)
    return area