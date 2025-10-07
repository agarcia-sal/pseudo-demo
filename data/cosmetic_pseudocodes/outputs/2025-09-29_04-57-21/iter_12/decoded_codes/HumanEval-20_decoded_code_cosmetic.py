from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    selected_pair: Optional[Tuple[int, int]] = None
    minimal_gap: Optional[int] = None
    outer_pos = 0
    n = len(list_of_numbers)

    while outer_pos < n - 1:
        outer_val = list_of_numbers[outer_pos]
        inner_pos = 0

        while inner_pos < n - 1:
            if outer_pos != inner_pos:
                inner_val = list_of_numbers[inner_pos]
                current_diff = abs(outer_val - inner_val)
                if minimal_gap is None or current_diff < minimal_gap:
                    minimal_gap = current_diff
                    selected_pair = (min(outer_val, inner_val), max(outer_val, inner_val))
            inner_pos += 1
        outer_pos += 1

    return selected_pair