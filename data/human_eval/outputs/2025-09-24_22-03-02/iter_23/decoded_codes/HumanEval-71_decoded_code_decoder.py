def triangle_area(a: float, b: float, c: float) -> float:
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return -1
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    area = area ** 0.5
    area = round(area, 2)
    return area