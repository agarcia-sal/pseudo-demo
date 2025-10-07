from typing import Any

def greatest_common_divisor(factor_x: int, factor_y: int) -> int:
    while factor_y != 0:
        pivot_value: int = factor_y
        factor_y = factor_x - ((factor_x // factor_y) * factor_y)
        factor_x = pivot_value
    return factor_x