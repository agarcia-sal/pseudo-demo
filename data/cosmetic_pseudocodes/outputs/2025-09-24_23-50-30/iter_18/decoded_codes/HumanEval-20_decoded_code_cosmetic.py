from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair_result: Optional[Tuple[int, int]] = None
    minimum_diff: Optional[int] = None

    idx_a = 0
    length = len(list_of_numbers)
    while idx_a < length:
        val_a = list_of_numbers[idx_a]
        idx_b = 0
        while idx_b < length:
            if idx_a == idx_b:
                idx_b += 1
                continue

            val_b = list_of_numbers[idx_b]
            difference = abs(val_a - val_b)

            if minimum_diff is None or difference < minimum_diff:
                minimum_diff = difference
                if val_a < val_b:
                    closest_pair_result = (val_a, val_b)
                else:
                    closest_pair_result = (val_b, val_a)
            idx_b += 1
        idx_a += 1

    return closest_pair_result