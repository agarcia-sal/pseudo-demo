from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator: int = 0
    length: int = len(sequence_of_numbers)
    while iterator < length:
        current_element: int = sequence_of_numbers[iterator]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator += 1
    return accumulator_sum, accumulator_product