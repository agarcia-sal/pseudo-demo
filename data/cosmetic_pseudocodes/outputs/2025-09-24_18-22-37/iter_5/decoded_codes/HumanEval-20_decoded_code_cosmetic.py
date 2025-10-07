from typing import List, Optional, Tuple

def find_closest_elements(numbers_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    distance_minimal: Optional[int] = None
    outer_idx: int = 0

    while outer_idx < len(numbers_list):
        val_outer: int = numbers_list[outer_idx]
        inner_idx: int = 0

        while inner_idx < len(numbers_list):
            val_inner: int = numbers_list[inner_idx]

            if outer_idx == inner_idx:
                inner_idx += 1
                continue

            diff: int = val_outer - val_inner
            abs_diff: int = -diff if diff < 0 else diff

            if distance_minimal is None:
                distance_minimal = abs_diff
                pair_closest = (val_outer, val_inner)
                if pair_closest[0] > pair_closest[1]:
                    pair_closest = (pair_closest[1], pair_closest[0])
            else:
                if abs_diff < distance_minimal:
                    distance_minimal = abs_diff
                    pair_closest = (val_outer, val_inner)
                    if pair_closest[0] > pair_closest[1]:
                        pair_closest = (pair_closest[1], pair_closest[0])

            inner_idx += 1
        outer_idx += 1

    return pair_closest