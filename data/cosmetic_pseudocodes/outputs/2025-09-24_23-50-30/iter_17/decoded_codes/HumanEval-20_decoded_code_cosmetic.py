from typing import List, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Tuple[int, int]:
    pair_result: Tuple[int, int] = ()
    smallest_gap: float = float('inf')
    length_var: int = len(list_of_numbers)
    idx_outer: int = 0

    while idx_outer < length_var:
        val_outer: int = list_of_numbers[idx_outer]
        idx_inner: int = 0

        while idx_inner < length_var:
            if idx_outer == idx_inner:
                idx_inner += 1
                continue

            val_inner: int = list_of_numbers[idx_inner]
            gap_current: int = val_outer - val_inner
            if gap_current < 0:
                gap_current = -gap_current

            if gap_current < smallest_gap:
                smallest_gap = gap_current
                if val_outer < val_inner:
                    pair_result = (val_outer, val_inner)
                else:
                    pair_result = (val_inner, val_outer)

            idx_inner += 1
        idx_outer += 1

    return pair_result