from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def accumulate_accumulators(current_index: int, length: int, acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if current_index >= length:
            return acc_sum, acc_prod
        current_element = list_of_integers[current_index]
        return accumulate_accumulators(
            current_index + 1,
            length,
            acc_sum + current_element,
            acc_prod * current_element
        )
    return accumulate_accumulators(0, len(list_of_integers), 0, 1)