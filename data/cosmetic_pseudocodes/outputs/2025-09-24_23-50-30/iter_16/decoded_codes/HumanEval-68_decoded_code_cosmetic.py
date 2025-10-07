from typing import List, Tuple, Union
import math


def pluck(collection_of_items: List[int]) -> List[Union[int, int]]:
    def find_min_even(items: List[int], idx: int, current_min: int, current_idx: int) -> Tuple[int, int]:
        if idx >= len(items):
            return current_min, current_idx
        candidate = items[idx]
        if candidate % 2 == 0 and candidate < current_min:
            return find_min_even(items, idx + 1, candidate, idx)
        return find_min_even(items, idx + 1, current_min, current_idx)

    if len(collection_of_items) < 1:
        return []

    filtered = [x for x in collection_of_items if x % 2 == 0]
    if not filtered:
        return []

    min_even_val, min_even_pos = find_min_even(collection_of_items, 0, math.inf, -1)
    return [min_even_val, min_even_pos]