from typing import List, Tuple

def sum_product(array_of_nums: List[int]) -> Tuple[int, int]:
    def recurse(index: int, acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if index >= len(array_of_nums):
            return acc_sum, acc_prod
        new_sum = acc_sum + array_of_nums[index]
        new_prod = acc_prod * array_of_nums[index]
        return recurse(index + 1, new_sum, new_prod)
    return recurse(0, 0, 1)