from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    index_counter: int = 0
    while index_counter < len(sequence_of_numbers):
        accumulator_sum += sequence_of_numbers[index_counter]
        accumulator_product *= sequence_of_numbers[index_counter]
        index_counter += 1
    return accumulator_sum, accumulator_product