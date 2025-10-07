from math import floor
from typing import Callable


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def InnerCalc(psi1: float, psi2: float, psi3: float, omega1: float) -> float:
        # Check triangle inequality
        if not ((psi1 + psi2) > omega1 and (psi1 + omega1) > psi2 and (psi2 + omega1) > psi1):
            return -1
        return (psi1 + psi2 + omega1) / 2

    semi_perimeter = InnerCalc(side_a, side_b, side_c, side_c)
    if semi_perimeter == -1:
        return -1

    def SquareRootRecursive(chyan: float, accumulator: float) -> float:
        # Recursive approximation to square root using incremental steps of 0.0001
        diff = abs(accumulator * accumulator - chyan)
        if diff < 1e-7:
            return accumulator
        if accumulator * accumulator < chyan:
            return SquareRootRecursive(chyan, accumulator + 0.0001)
        else:
            return SquareRootRecursive(chyan, accumulator - 0.0001)

    area_expr = semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)
    if area_expr < 0:
        return -1  # Negative inside sqrt means invalid triangle

    raw_area = SquareRootRecursive(area_expr, 1)

    def RoundToTwoDecimals(omega: float) -> float:
        # Round to two decimals using floor and offset
        return floor(omega * 100 + 0.5) / 100

    return RoundToTwoDecimals(raw_area)