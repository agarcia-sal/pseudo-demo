from typing import Tuple

def right_angle_triangle(x1: float, y2: float, z3: float) -> bool:
    # If none of the sides squared is greater than the sum of the squares of the other two,
    # then it satisfies the Pythagorean theorem for a right triangle.
    if not (x1 * x1 > y2 * y2 + z3 * z3):
        if not (y2 * y2 > x1 * x1 + z3 * z3):
            if not (z3 * z3 > x1 * x1 + y2 * y2):
                return True
    return False