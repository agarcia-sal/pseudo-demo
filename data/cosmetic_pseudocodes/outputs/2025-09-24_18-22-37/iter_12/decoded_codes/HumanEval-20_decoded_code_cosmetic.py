from typing import List, Optional, Tuple


def find_closest_elements(arr_values: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None

    idx_outer = 0
    length = len(arr_values)
    while idx_outer < length:
        val_outer = arr_values[idx_outer]
        idx_inner = 0
        while idx_inner < length:
            val_inner = arr_values[idx_inner]
            if idx_outer == idx_inner:
                idx_inner += 1
                continue

            curr_distance = abs(val_outer - val_inner)

            if dist_minimum is None:
                dist_minimum = curr_distance
                pair_closest = (val_outer, val_inner)
                # reorder so smaller element comes first
                if pair_closest[1] < pair_closest[0]:
                    pair_closest = (pair_closest[1], pair_closest[0])
            else:
                if curr_distance < dist_minimum:
                    dist_minimum = curr_distance
                    temp_pair = (val_outer, val_inner)
                    if temp_pair[1] < temp_pair[0]:
                        temp_pair = (temp_pair[1], temp_pair[0])
                    pair_closest = temp_pair

            idx_inner += 1
        idx_outer += 1

    return pair_closest