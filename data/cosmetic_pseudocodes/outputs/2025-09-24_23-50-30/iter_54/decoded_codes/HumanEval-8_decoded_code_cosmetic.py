from typing import Iterable, Tuple

def sum_product(collection_of_numbers: Iterable[int]) -> Tuple[int, int]:
    numbers = list(collection_of_numbers)  # Ensure indexable

    def helper(index: int, current_sum: int, current_product: int) -> Tuple[int, int]:
        if index >= len(numbers):
            return current_sum, current_product
        element = numbers[index]
        return helper(index + 1, current_sum + element, current_product * element)

    return helper(0, 0, 1)