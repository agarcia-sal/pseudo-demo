from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_nearest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None
    pos_outer = 0
    length = len(sequence)

    while pos_outer < length:
        val_outer = sequence[pos_outer]
        pos_inner = 0
        while pos_inner < length:
            if pos_outer != pos_inner:
                val_inner = sequence[pos_inner]
                dist_current = abs(val_outer - val_inner)
                if dist_minimum is None or dist_current < dist_minimum:
                    dist_minimum = dist_current
                    pair_nearest = tuple(sorted((val_outer, val_inner)))
            pos_inner += 1
        pos_outer += 1

    return pair_nearest