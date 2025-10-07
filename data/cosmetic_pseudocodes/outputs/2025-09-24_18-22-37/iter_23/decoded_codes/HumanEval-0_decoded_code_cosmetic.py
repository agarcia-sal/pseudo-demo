from typing import Sequence


def has_close_elements(some_sequence: Sequence[int], limit: int) -> bool:
    outer_pos: int = 0
    while outer_pos < len(some_sequence):
        first_entry: int = some_sequence[outer_pos]
        inner_pos: int = 0
        while inner_pos < len(some_sequence):
            second_entry: int = some_sequence[inner_pos]
            if outer_pos != inner_pos:
                dist_calc: int = first_entry - second_entry
                if dist_calc < 0:
                    dist_calc = -dist_calc
                if dist_calc < limit:
                    return True
            inner_pos += 1
        outer_pos += 1
    return False