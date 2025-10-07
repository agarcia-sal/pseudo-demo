from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: Optional[int] = None
    idx_outer = 0
    length = len(list_of_numbers)
    while idx_outer < length:
        val_outer = list_of_numbers[idx_outer]
        idx_inner = 0
        while idx_inner < length:
            val_inner = list_of_numbers[idx_inner]
            if idx_outer == idx_inner:
                idx_inner += 1
                continue
            current_distance = val_outer - val_inner
            if current_distance < 0:
                current_distance = -current_distance
            if minimum_distance is None or current_distance < minimum_distance:
                minimum_distance = current_distance
                closest_pair = (val_outer, val_inner)
                if closest_pair[0] > closest_pair[1]:
                    closest_pair = (closest_pair[1], closest_pair[0])
            idx_inner += 1
        idx_outer += 1
    return closest_pair