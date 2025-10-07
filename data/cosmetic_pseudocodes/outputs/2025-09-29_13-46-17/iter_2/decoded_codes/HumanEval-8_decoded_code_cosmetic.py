from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def helper(index: int, current_sum: int, current_product: int) -> Tuple[int, int]:
        if index == len(list_of_integers):
            return current_sum, current_product
        next_sum = current_sum + list_of_integers[index]
        next_product = current_product * list_of_integers[index]
        return helper(index + 1, next_sum, next_product)
    return helper(0, 0, 1)