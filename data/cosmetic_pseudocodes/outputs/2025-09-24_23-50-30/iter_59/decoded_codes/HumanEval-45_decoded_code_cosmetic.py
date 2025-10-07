def triangle_area(a: float, b: float) -> float:
    if a != 0 and b != 0:
        return (b / 2.0) * a
    else:
        return (a * b) / 2.0