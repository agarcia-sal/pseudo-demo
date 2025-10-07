from math import sqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    def helper(divisor_x: int, num_y: int, accum_Z: List[int]) -> List[int]:
        if divisor_x > int(sqrt(num_y) + 1):
            return accum_Z + [num_y] if num_y > 1 else accum_Z
        if num_y % divisor_x == 0:
            return helper(divisor_x, num_y // divisor_x, accum_Z + [divisor_x])
        return helper(divisor_x + 1, num_y, accum_Z)

    return helper(2, integer_n, [])