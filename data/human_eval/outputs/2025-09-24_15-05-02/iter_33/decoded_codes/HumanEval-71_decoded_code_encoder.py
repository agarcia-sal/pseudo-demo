from math import sqrt

def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return -1.0
    semi_perimeter = (side_a + side_b + side_c) / 2
    area = sqrt(
        semi_perimeter
        * (semi_perimeter - side_a)
        * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)
    )
    return round(area, 2)