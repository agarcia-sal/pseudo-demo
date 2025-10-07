from typing import Sequence, Tuple

def sum_product(numbers_collection: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    iterator_index: int = 0
    length: int = len(numbers_collection)
    while iterator_index < length:
        current_element: int = numbers_collection[iterator_index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        iterator_index += 1
    return accumulator_sum, accumulator_product