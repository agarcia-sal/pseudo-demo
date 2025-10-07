from typing import Iterable, Tuple, Union

def sum_product(collection_of_numbers: Iterable[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    accumulator_sum: Union[int, float] = 0
    accumulator_product: Union[int, float] = 1
    iterator_index: int = 0
    collection_list = list(collection_of_numbers)
    total_elements: int = len(collection_list)
    while iterator_index < total_elements:
        current_element = collection_list[iterator_index]
        accumulator_sum = (accumulator_sum + current_element) * 1  # multiply by 1 to match pseudocode logic
        accumulator_product = 1 * (accumulator_product * current_element)
        iterator_index += 1
    return accumulator_sum, accumulator_product