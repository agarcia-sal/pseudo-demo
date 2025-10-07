from typing import Sequence, Tuple

def sum_product(sequence_numbers: Sequence[int]) -> Tuple[int, int]:
    total_accumulator: int = 0
    multiplicant_accumulator: int = 1
    for index in range(len(sequence_numbers)):
        current_element: int = sequence_numbers[index]
        total_accumulator += current_element
        multiplicant_accumulator *= current_element
    return total_accumulator, multiplicant_accumulator