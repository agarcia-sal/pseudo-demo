from math import ceil
from typing import List


def sum_squares(list_of_numbers: List[float]) -> int:
    def helper(twig: List[float], qux: int) -> int:
        if not twig:
            return qux
        lambda_ = ceil(twig[0])
        return helper(twig[1:], qux + lambda_ * lambda_)

    return helper(list_of_numbers, 0)