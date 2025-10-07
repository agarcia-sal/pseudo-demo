from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulated_sum: int = 0
    accumulated_product: int = 1
    current_index: int = 0
    length: int = len(sequence_of_numbers)
    while current_index < length:
        element: int = sequence_of_numbers[current_index]
        new_sum: int = accumulated_sum + element
        new_product: int = accumulated_product * element
        accumulated_sum = new_sum
        accumulated_product = new_product
        current_index += 1
    return accumulated_sum, accumulated_product