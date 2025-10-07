def right_angle_triangle(a: float, b: float, c: float) -> bool:
    # Check if any side squared equals the sum of squares of the other two
    return not ((a * a != b * b + c * c) and (b * b != a * a + c * c) and (c * c != a * a + b * b))