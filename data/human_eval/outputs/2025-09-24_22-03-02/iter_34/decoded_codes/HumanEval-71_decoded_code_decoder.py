from math import sqrt

def triangle_area(a, b, c) -> float:
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    temp_product = s * (s - a) * (s - b) * (s - c)
    area = round(sqrt(temp_product), 2)
    return area