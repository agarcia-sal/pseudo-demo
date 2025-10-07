from typing import Sequence, Optional, Tuple

def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    min_dist: Optional[int] = None
    best_pair: Optional[Tuple[int, int]] = None

    for outer_idx in range(len(numbers_collection)):
        val_outer = numbers_collection[outer_idx]
        for inner_idx in range(len(numbers_collection)):
            val_inner = numbers_collection[inner_idx]
            if outer_idx != inner_idx:
                diff_abs = abs(val_outer - val_inner)
                if min_dist is None or diff_abs < min_dist:
                    min_dist = diff_abs
                    if val_outer < val_inner:
                        best_pair = (val_outer, val_inner)
                    else:
                        best_pair = (val_inner, val_outer)

    return best_pair