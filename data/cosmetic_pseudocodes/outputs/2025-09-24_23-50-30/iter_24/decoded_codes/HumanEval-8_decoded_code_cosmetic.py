from typing import Sequence, List

def sum_product(sequence: Sequence[int]) -> List[int]:
    def accumulate(index: int, total_sum: int, total_product: int) -> List[int]:
        if index >= len(sequence):
            return [total_sum, total_product]
        current_element = sequence[index]
        return accumulate(index + 1, total_sum + current_element, total_product * current_element)
    return accumulate(0, 0, 1)