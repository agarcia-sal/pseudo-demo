from typing import Sequence, Optional, Tuple


def find_closest_elements(collection_of_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for outer_idx in range(len(collection_of_values)):
        value_outer = collection_of_values[outer_idx]

        for inner_idx in range(len(collection_of_values)):
            if outer_idx != inner_idx:
                value_inner = collection_of_values[inner_idx]
                diff_temp = value_outer - value_inner
                absolute_diff = -diff_temp if diff_temp < 0 else diff_temp

                if smallest_gap is None:
                    smallest_gap = absolute_diff
                    if value_outer > value_inner:
                        result_pair = (value_inner, value_outer)
                    else:
                        result_pair = (value_outer, value_inner)
                elif absolute_diff < smallest_gap:
                    smallest_gap = absolute_diff
                    if value_outer > value_inner:
                        result_pair = (value_inner, value_outer)
                    else:
                        result_pair = (value_outer, value_inner)

    return result_pair