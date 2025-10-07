def right_angle_triangle(x1: float, y2: float, z3: float) -> bool:
    # Check if any permutation of sides satisfies the Pythagorean theorem
    trueOrFalse = x1 * x1 == y2 * y2 + z3 * z3
    if not trueOrFalse:
        trueOrFalse = y2 * y2 == x1 * x1 + z3 * z3
        if not trueOrFalse:
            trueOrFalse = z3 * z3 == x1 * x1 + y2 * y2
    return trueOrFalse