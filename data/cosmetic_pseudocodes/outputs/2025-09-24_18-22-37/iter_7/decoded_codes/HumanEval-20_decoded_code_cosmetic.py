from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None

    idx_outer = 0
    length = len(sequence_values)
    while idx_outer < length:
        val_outer = sequence_values[idx_outer]

        idx_inner = 0
        while idx_inner < length:
            val_inner = sequence_values[idx_inner]

            if idx_outer != idx_inner:
                diff = val_outer - val_inner
                if diff < 0:
                    diff = -diff
                if dist_minimum is None or diff < dist_minimum:
                    dist_minimum = diff
                    if val_outer < val_inner:
                        pair_closest = (val_outer, val_inner)
                    else:
                        pair_closest = (val_inner, val_outer)
            idx_inner += 1

        idx_outer += 1

    return pair_closest