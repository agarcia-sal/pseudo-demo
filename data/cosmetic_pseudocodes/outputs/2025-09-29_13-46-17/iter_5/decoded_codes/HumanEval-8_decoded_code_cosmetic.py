from typing import Sequence, Tuple

def sum_product(sequence_data: Sequence[int]) -> Tuple[int, int]:
    def accumulate(index_val: int, cum_sum: int, cum_prod: int) -> Tuple[int, int]:
        if not (index_val < len(sequence_data)):
            return cum_sum, cum_prod
        current_element = sequence_data[index_val]
        new_sum = cum_sum + current_element
        new_prod = cum_prod * current_element
        return accumulate(index_val + 1, new_sum, new_prod)
    return accumulate(0, 0, 1)