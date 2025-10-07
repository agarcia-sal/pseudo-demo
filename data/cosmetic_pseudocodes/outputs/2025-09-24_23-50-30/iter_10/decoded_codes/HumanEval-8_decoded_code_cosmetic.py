from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    def helper(index: int, accum_sum: int, accum_prod: int) -> Tuple[int, int]:
        if index == len(numbers):
            return accum_sum, accum_prod
        return helper(index + 1, accum_sum + numbers[index], accum_prod * numbers[index])

    return helper(0, 0, 1)