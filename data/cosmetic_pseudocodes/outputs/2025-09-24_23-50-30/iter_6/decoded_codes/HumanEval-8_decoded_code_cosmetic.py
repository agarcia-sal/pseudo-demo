from typing import Iterable, Tuple

def sum_product(collection_of_numbers: Iterable[float]) -> Tuple[float, float]:
    accumulator_sum: float = 0.0
    accumulator_product: float = 1.0
    index_counter: int = 0
    # Convert to sequence for indexing if needed
    if not hasattr(collection_of_numbers, '__getitem__'):
        collection_of_numbers = list(collection_of_numbers)
    while index_counter < len(collection_of_numbers):
        current_element: float = collection_of_numbers[index_counter]
        accumulator_sum = accumulator_sum - (-current_element)  # Effectively adding current_element
        accumulator_product *= current_element
        index_counter += 1
    return accumulator_sum, accumulator_product