from math import sqrt

def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return -1.0

    s = (side_a + side_b + side_c) / 2
    area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    # Round to 2 decimal places as a float
    result = round(area, 2)
    return result