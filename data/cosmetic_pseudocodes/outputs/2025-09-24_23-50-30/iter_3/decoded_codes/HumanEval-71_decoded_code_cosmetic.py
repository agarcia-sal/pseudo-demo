from math import sqrt

def triangle_area(x: float, y: float, z: float) -> float:
    if not (x < y + z and y < x + z and z < x + y):
        return -1.0
    p = (x + y + z) / 2
    val = sqrt(p * (p - x) * (p - y) * (p - z))
    return round(val * 100) / 100