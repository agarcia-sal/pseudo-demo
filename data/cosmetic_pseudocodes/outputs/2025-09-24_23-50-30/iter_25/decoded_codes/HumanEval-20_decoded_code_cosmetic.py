from typing import Sequence, Optional, Tuple

def find_closest_elements(sequence_of_values: Sequence[float]) -> Optional[Tuple[float, float]]:
    pair_closest: Optional[Tuple[float, float]] = None
    distance_minimal: Optional[float] = None
    pos_outer: int = 0
    length: int = len(sequence_of_values)

    while pos_outer < length:
        val_outer = sequence_of_values[pos_outer]
        pos_inner = 0

        while pos_inner < length:
            if pos_outer != pos_inner:
                val_inner = sequence_of_values[pos_inner]
                diff_new = abs(val_outer - val_inner)
                if distance_minimal is None or diff_new < distance_minimal:
                    distance_minimal = diff_new
                    pair_closest = tuple(sorted((val_outer, val_inner)))
            pos_inner += 1

        pos_outer += 1

    return pair_closest