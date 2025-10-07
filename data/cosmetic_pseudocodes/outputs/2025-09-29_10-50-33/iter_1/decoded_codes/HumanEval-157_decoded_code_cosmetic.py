def right_angle_triangle(a: float, b: float, c: float) -> bool:
    return (
        a * a == b * b + c * c
        or b * b == a * a + c * c
        or c * c == a * a + b * b
    )