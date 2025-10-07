from typing import List, Tuple


def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def helper(index: int, acc_sum: int, acc_product: int) -> Tuple[int, int]:
        if index == len(list_of_integers):
            return acc_sum, acc_product
        current = list_of_integers[index]
        return helper(index + 1, acc_sum + current, acc_product * current)

    return helper(0, 0, 1)