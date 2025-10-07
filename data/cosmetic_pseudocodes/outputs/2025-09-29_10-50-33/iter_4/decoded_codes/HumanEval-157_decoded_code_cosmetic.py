def right_angle_triangle(x1: float, y2: float, z3: float) -> bool:
    if not (x1 * x1 != y2 * y2 + z3 * z3):
        return True
    if not (y2 * y2 != x1 * x1 + z3 * z3):
        return True
    if not (z3 * z3 != x1 * x1 + y2 * y2):
        return True
    return False