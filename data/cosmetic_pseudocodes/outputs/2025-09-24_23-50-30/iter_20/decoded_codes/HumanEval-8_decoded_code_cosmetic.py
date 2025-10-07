from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator_index: int = 0
    while not (iterator_index >= len(sequence_of_numbers)):
        current_element: int = sequence_of_numbers[iterator_index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator_index += 1
    return accumulator_sum, accumulator_product