from typing import Sequence, Tuple

def sum_product(numbers_collection: Sequence[int]) -> Tuple[int, int]:
    accumulator_sum: int = 0
    accumulator_product: int = 1
    current_index: int = 0
    collection_length: int = len(numbers_collection)
    while current_index < collection_length:
        current_element: int = numbers_collection[current_index]
        accumulator_sum += current_element
        accumulator_product *= current_element
        current_index += 1
    return accumulator_sum, accumulator_product