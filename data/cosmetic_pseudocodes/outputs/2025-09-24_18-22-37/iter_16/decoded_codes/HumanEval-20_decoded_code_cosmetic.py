from typing import List, Optional, Tuple


def find_closest_elements(locals_list: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None
    idx_outer = 0

    while idx_outer < len(locals_list):
        val_outer = locals_list[idx_outer]
        idx_inner = 0

        while idx_inner < len(locals_list):
            val_inner = locals_list[idx_inner]

            if idx_outer != idx_inner:
                difference_delta = val_outer - val_inner
                absolute_diff = abs(difference_delta)

                if smallest_gap is None or absolute_diff < smallest_gap:
                    smallest_gap = absolute_diff
                    # Sort pair so smaller value first
                    if val_inner <= val_outer:
                        result_pair = (val_inner, val_outer)
                    else:
                        result_pair = (val_outer, val_inner)

            idx_inner += 1
        idx_outer += 1

    return result_pair