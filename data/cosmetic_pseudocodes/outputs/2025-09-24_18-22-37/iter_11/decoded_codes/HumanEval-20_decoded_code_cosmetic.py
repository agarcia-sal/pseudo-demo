from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    outer_idx = 0
    length = len(list_of_numbers)
    while outer_idx < length:
        val_outer = list_of_numbers[outer_idx]
        inner_idx = 0
        while inner_idx < length:
            val_inner = list_of_numbers[inner_idx]

            if outer_idx == inner_idx:
                inner_idx += 1
                continue

            current_diff = val_outer - val_inner
            if current_diff < 0:
                current_diff = -current_diff

            if smallest_gap is None:
                smallest_gap = current_diff
                if val_inner > val_outer:
                    result_pair = (val_outer, val_inner)
                else:
                    result_pair = (val_inner, val_outer)
            elif current_diff < smallest_gap:
                smallest_gap = current_diff
                if val_outer < val_inner:
                    result_pair = (val_outer, val_inner)
                else:
                    result_pair = (val_inner, val_outer)

            inner_idx += 1
        outer_idx += 1

    return result_pair