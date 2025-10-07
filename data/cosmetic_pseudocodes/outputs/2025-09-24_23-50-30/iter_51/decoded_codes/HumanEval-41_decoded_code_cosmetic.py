from typing import Callable

def car_race_collision(scalar_val: int) -> int:
    def inner_expansion(accrued: int, base: int, count: int) -> int:
        if count == 0:
            return accrued
        return inner_expansion(accrued + base + base * (count - 1), base, count - 1)

    base_val = scalar_val * scalar_val // scalar_val  # integer division consistent with pseudocode arithmetic
    return inner_expansion(0, base_val, scalar_val)