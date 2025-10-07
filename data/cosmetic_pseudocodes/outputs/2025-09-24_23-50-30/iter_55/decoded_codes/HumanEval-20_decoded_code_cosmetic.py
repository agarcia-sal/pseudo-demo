from typing import Optional, Sequence, Tuple


def find_closest_elements(sequence_of_values: Sequence[float]) -> Optional[Tuple[float, float]]:
    best_elements: Optional[Tuple[float, float]] = None
    smallest_gap: Optional[float] = None

    outer_cursor = 0
    length = len(sequence_of_values)

    while outer_cursor < length:
        item_outer = sequence_of_values[outer_cursor]

        inner_cursor = 0
        while inner_cursor < length:
            if outer_cursor != inner_cursor:
                item_inner = sequence_of_values[inner_cursor]
                candidate_gap = abs(item_outer - item_inner)

                if smallest_gap is None or candidate_gap < smallest_gap:
                    smallest_gap = candidate_gap
                    best_elements = tuple(sorted((item_outer, item_inner)))

            inner_cursor += 1
        outer_cursor += 1

    return best_elements