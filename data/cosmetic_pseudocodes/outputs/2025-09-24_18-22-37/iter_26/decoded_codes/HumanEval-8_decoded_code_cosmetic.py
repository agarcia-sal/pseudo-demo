from typing import Iterable, Tuple

def sum_product(collection_of_numbers: Iterable[int]) -> Tuple[int, int]:
    aggregate_sum: int = 0
    aggregate_product: int = 1
    idx: int = 0
    collection_list = list(collection_of_numbers)  # Support indexing

    while idx < len(collection_list):
        current_number: int = collection_list[idx]
        aggregate_sum += current_number
        aggregate_product *= current_number
        idx += 1

    return aggregate_sum, aggregate_product