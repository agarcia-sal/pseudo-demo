from typing import Iterable, Tuple

def sum_product(collection: Iterable[int]) -> Tuple[int, int]:
    idx: int = 0
    total_sum: int = 0
    total_prod: int = 1
    collection_list = list(collection)  # Ensures repeated access by index
    while idx < len(collection_list):
        total_sum += collection_list[idx]
        total_prod *= collection_list[idx]
        idx += 1
    return total_sum, total_prod