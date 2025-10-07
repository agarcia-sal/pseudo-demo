from typing import List, Optional, Tuple


def find_closest_elements(numbers_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None

    idx_outer = 0
    length = len(numbers_list)
    while idx_outer < length:
        val_outer = numbers_list[idx_outer]
        idx_inner = 0
        while idx_inner < length:
            if idx_outer != idx_inner:
                val_inner = numbers_list[idx_inner]
                dist_new = abs(val_outer - val_inner)
                if dist_minimum is None or dist_new < dist_minimum:
                    dist_minimum = dist_new
                    pair_closest = tuple(sorted((val_outer, val_inner)))
            idx_inner += 1
        idx_outer += 1

    return pair_closest