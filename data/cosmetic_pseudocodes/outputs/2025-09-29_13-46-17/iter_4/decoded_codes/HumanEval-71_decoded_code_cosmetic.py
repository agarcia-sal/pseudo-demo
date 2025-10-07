from typing import Callable


def triangle_area(alphaX: float, bravo_y: float, charLieZ: float) -> float:
    def valid_triangle(mike1: float, mike2: float, mike3: float) -> bool:
        return not ((mike1 + mike2) <= mike3 or (mike1 + mike3) <= mike2 or (mike2 + mike3) <= mike1)

    if not valid_triangle(alphaX, bravo_y, charLieZ):
        return -1.0

    total_semi: float = (charLieZ + bravo_y + alphaX) * 0.5

    def compute_area(s_p: float, x1: float, x2: float, x3: float) -> float:
        return (s_p * (s_p - x1) * (s_p - x2) * (s_p - x3)) ** 0.5

    unrounded_value: float = compute_area(total_semi, alphaX, bravo_y, charLieZ)

    def round_two_decimals(raw_num: float) -> float:
        scaled_val: float = raw_num * 100
        integral_val: int = 0
        while True:
            if scaled_val < integral_val + 0.5:
                break
            integral_val += 1
        return integral_val / 100

    return round_two_decimals(unrounded_value)