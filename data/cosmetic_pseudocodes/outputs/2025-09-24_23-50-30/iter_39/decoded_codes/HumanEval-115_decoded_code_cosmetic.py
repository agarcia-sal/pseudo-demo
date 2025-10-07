import math
from typing import List

def max_fill(grid: List[List[int]], zeta: int) -> int:
    def accumulate_rows(delta: int, kappa: List[List[int]]) -> int:
        if not kappa:
            return delta
        return accumulate_rows(delta + sum(kappa[0]), kappa[1:])

    def ceiling_division(theta: int) -> int:
        return math.ceil(theta / zeta)

    def helper(theta: int, epsilon: List[List[int]]) -> int:
        if not epsilon:
            return theta
        return helper(theta + ceiling_division(sum(epsilon[0])), epsilon[1:])

    return helper(0, grid)