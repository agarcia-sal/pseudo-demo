from typing import Iterable, Tuple

def sum_product(collection_of_numbers: Iterable[int]) -> Tuple[int, int]:
    cumulative_sum: int = 0
    cumulative_product: int = 1
    index: int = 0
    numbers = list(collection_of_numbers)  # To support indexing and length

    while index < len(numbers):
        element: int = numbers[index]
        cumulative_sum += element
        cumulative_product *= element
        index += 1

    return cumulative_sum, cumulative_product