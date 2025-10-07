from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    best_diff: Optional[int] = None

    for outer_idx, outer_val in enumerate(list_of_numbers):
        for inner_idx, inner_val in enumerate(list_of_numbers):
            if outer_idx != inner_idx:
                current_diff = abs(outer_val - inner_val)
                if best_diff is None or current_diff < best_diff:
                    best_diff = current_diff
                    best_match = (min(outer_val, inner_val), max(outer_val, inner_val))

    return best_match