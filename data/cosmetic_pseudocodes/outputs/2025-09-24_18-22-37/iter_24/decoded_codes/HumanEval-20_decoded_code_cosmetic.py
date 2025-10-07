from typing import Optional, Tuple, Sequence


def find_closest_elements(collection_of_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    best_pair_result: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None
    outer_idx: int = 0

    while outer_idx < len(collection_of_values):
        current_outer_value = collection_of_values[outer_idx]
        inner_idx = 0

        while inner_idx < len(collection_of_values):
            current_inner_value = collection_of_values[inner_idx]

            if outer_idx == inner_idx:
                pass  # skip same index comparison
            elif smallest_gap is None:
                gap_measure = abs(current_outer_value - current_inner_value)
                smallest_gap = gap_measure
                best_pair_result = (min(current_outer_value, current_inner_value),
                                    max(current_outer_value, current_inner_value))
            else:
                computed_gap = abs(current_inner_value - current_outer_value)
                if computed_gap < smallest_gap:
                    smallest_gap = computed_gap
                    best_pair_result = (min(current_outer_value, current_inner_value),
                                        max(current_outer_value, current_inner_value))

            inner_idx += 1
        outer_idx += 1

    return best_pair_result