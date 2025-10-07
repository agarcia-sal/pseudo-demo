from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    aggregate_sum: int = 0
    aggregate_product: int = 1

    iterator_index: int = 0
    while iterator_index < len(list_of_integers):
        current_element: int = list_of_integers[iterator_index]
        aggregate_sum += current_element
        aggregate_product *= current_element
        iterator_index += 1

    return aggregate_sum, aggregate_product