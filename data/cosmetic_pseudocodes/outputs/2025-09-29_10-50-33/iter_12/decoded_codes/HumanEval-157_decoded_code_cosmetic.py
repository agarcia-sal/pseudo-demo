def right_angle_triangle(x1: float, y2: float, z3: float) -> bool:
    # Check if any of the three sides satisfies the Pythagorean theorem
    return not (
        (x1 * x1 != y2 * y2 + z3 * z3) and
        (y2 * y2 != x1 * x1 + z3 * z3) and
        (z3 * z3 != x1 * x1 + y2 * y2)
    )