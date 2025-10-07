from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    index: int = 0
    while index < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[index]
        temp_sum: int = total_sum + current_element
        total_sum = temp_sum
        total_product *= current_element
        index += 1
    return total_sum, total_product