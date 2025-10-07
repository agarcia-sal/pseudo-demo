from typing import Sequence, Tuple

def sum_product(container_elements: Sequence[int]) -> Tuple[int, int]:
    def helper(index: int, acc_sum: int, acc_product: int) -> Tuple[int, int]:
        if index == len(container_elements):
            return acc_sum, acc_product
        return helper(index + 1, acc_sum + container_elements[index], acc_product * container_elements[index])
    return helper(0, 0, 1)