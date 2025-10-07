from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence_of_values: Sequence[float]) -> Optional[Tuple[float, float]]:
    best_match: Optional[Tuple[float, float]] = None
    smallest_gap: Optional[float] = None
    outer_cursor: int = 0

    while outer_cursor < len(sequence_of_values):
        outer_val = sequence_of_values[outer_cursor]
        inner_cursor = 0

        while inner_cursor < len(sequence_of_values):
            inner_val = sequence_of_values[inner_cursor]

            if outer_cursor == inner_cursor:
                inner_cursor += 1
                continue
            else:
                difference_abs = outer_val - inner_val
                if difference_abs < 0:
                    difference_abs = -difference_abs

                if (smallest_gap is not None) and (difference_abs < smallest_gap):
                    smallest_gap = difference_abs
                    if outer_val < inner_val:
                        best_match = (outer_val, inner_val)
                    else:
                        best_match = (inner_val, outer_val)
                elif smallest_gap is None:
                    smallest_gap = difference_abs
                    if outer_val < inner_val:
                        best_match = (outer_val, inner_val)
                    else:
                        best_match = (inner_val, outer_val)

            inner_cursor += 1
        outer_cursor += 1

    return best_match