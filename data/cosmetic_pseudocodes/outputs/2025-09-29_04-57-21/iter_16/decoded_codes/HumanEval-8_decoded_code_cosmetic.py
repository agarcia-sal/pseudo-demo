from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    aggregate_sum: int = 0
    aggregate_product: int = 1
    iterator = iter(list_of_integers)
    while True:
        try:
            current_element = next(iterator)
            aggregate_sum += current_element
            aggregate_product *= current_element
        except StopIteration:
            break
    return aggregate_sum, aggregate_product