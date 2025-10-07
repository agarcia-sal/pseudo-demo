from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    def loop(iter_seq: Sequence[int], acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if not iter_seq:
            return acc_sum, acc_prod
        current_element, *remaining_elements = iter_seq
        return loop(remaining_elements, acc_sum + current_element, acc_prod * current_element)
    return loop(sequence_of_numbers, 0, 1)