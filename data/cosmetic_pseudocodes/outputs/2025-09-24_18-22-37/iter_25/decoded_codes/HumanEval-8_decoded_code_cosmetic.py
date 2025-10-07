from typing import Sequence, Tuple

def sum_product(collection_of_numbers: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    idx_counter: int = 0
    length = len(collection_of_numbers)
    while idx_counter < length:
        current_element = collection_of_numbers[idx_counter]
        accumulator_sum += current_element
        accumulator_product *= current_element
        idx_counter += 1
    return accumulator_sum, accumulator_product