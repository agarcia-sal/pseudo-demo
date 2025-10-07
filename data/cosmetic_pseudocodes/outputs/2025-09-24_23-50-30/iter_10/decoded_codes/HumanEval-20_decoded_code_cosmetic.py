from typing import Iterable, Optional, Tuple, Union

def find_closest_elements(numbers_collection: Iterable[Union[int, float]]) -> Optional[Tuple[Union[int, float], Union[int, float]]]:
    best_pair: Optional[Tuple[Union[int, float], Union[int, float]]] = None
    smallest_gap: Optional[Union[int, float]] = None
    numbers_list = list(numbers_collection)  # Ensure multiple passes and indexing
    for i, val_i in enumerate(numbers_list):
        for j, val_j in enumerate(numbers_list):
            if i != j:
                current_gap = abs(val_i - val_j)
                if smallest_gap is None or current_gap < smallest_gap:
                    smallest_gap = current_gap
                    best_pair = tuple(sorted((val_i, val_j)))
    return best_pair