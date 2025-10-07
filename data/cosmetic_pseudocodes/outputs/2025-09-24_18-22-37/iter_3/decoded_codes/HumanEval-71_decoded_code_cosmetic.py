from math import sqrt, floor

def triangle_area(x: float, y: float, z: float) -> float:
    if not (x + y > z and x + z > y and y + z > x):
        return -1
    p: float = (x + y + z) / 2
    area_raw: float = sqrt(p * (p - x) * (p - y) * (p - z))
    result: float = floor(area_raw * 100 + 0.5) / 100
    return result