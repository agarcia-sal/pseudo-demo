from typing import Iterable, Tuple

def sum_product(numbers_collection: Iterable[int]) -> Tuple[int, int]:
    cumulative_sum: int = 0
    cumulative_product: int = 1
    index: int = 0
    numbers_list = list(numbers_collection)  # Ensure indexable
    while index < len(numbers_list):
        current_number = numbers_list[index]
        cumulative_sum += current_number
        cumulative_product *= current_number
        index += 1
    return cumulative_sum, cumulative_product