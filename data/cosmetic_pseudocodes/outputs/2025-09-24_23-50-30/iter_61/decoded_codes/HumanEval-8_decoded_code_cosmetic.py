from typing import List, Tuple


def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def recurse(index_stack: List[int], acc_sum: int, acc_product: int) -> Tuple[int, int]:
        if not index_stack:
            return acc_sum, acc_product
        head_element = index_stack[0]
        tail_stack = index_stack[1:]
        return recurse(tail_stack, acc_sum + head_element, acc_product * head_element)

    return recurse(list_of_integers, 0, 1)