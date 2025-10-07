from typing import List, Optional, Tuple

def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    best_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for outer_index, outer_value in enumerate(array_of_values):
        for inner_index, inner_value in enumerate(array_of_values):
            if outer_index != inner_index:
                current_distance = abs(outer_value - inner_value)
                if smallest_gap is None or current_distance < smallest_gap:
                    smallest_gap = current_distance
                    if outer_value < inner_value:
                        best_pair = (outer_value, inner_value)
                    else:
                        best_pair = (inner_value, outer_value)

    return best_pair