from typing import Optional, Tuple, Sequence


def find_closest_elements(array_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    value_min_diff: Optional[int] = None
    counter_outer: int = 0

    while counter_outer < len(array_values):
        current_outer = array_values[counter_outer]
        counter_inner: int = 0

        while counter_inner < len(array_values):
            current_inner = array_values[counter_inner]

            if counter_outer != counter_inner:
                if value_min_diff is None:
                    value_min_diff = abs(current_outer - current_inner)
                    pair_closest = (min(current_outer, current_inner), max(current_outer, current_inner))
                else:
                    candidate_diff = abs(current_outer - current_inner)
                    if candidate_diff < value_min_diff:
                        value_min_diff = candidate_diff
                        pair_closest = (min(current_outer, current_inner), max(current_outer, current_inner))
            counter_inner += 1
        counter_outer += 1

    return pair_closest