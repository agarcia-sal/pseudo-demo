import math

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = round(area, 2)
    return area