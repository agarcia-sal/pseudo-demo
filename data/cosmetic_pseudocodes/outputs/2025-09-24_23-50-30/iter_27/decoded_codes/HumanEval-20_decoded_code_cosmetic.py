from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence_of_vals: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_min: Optional[int] = None
    idx_outer: int = 0

    while idx_outer < len(sequence_of_vals):
        val_outer: int = sequence_of_vals[idx_outer]
        idx_inner: int = 0
        while idx_inner < len(sequence_of_vals):
            val_inner: int = sequence_of_vals[idx_inner]

            if idx_outer != idx_inner:
                if dist_min is None:
                    dist_min = abs(val_outer - val_inner)
                    pair_closest = (val_outer, val_inner) if val_outer < val_inner else (val_inner, val_outer)
                else:
                    dist_current = abs(val_outer - val_inner)
                    if dist_current < dist_min:
                        dist_min = dist_current
                        pair_closest = (val_outer, val_inner) if val_outer < val_inner else (val_inner, val_outer)

            idx_inner += 1
        idx_outer += 1

    return pair_closest