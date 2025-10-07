from typing import List, Optional, Tuple


def find_closest_elements(array_input: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for outer_idx, outer_val in enumerate(array_input):
        for inner_idx, inner_val in enumerate(array_input):
            proceed_check: bool = outer_idx != inner_idx

            if proceed_check:
                current_diff = abs(outer_val - inner_val)
                if smallest_gap is None or current_diff < smallest_gap:
                    smallest_gap = current_diff
                    # Order pair ascendingly
                    if outer_val < inner_val:
                        assembled_pair = (outer_val, inner_val)
                    else:
                        assembled_pair = (inner_val, outer_val)
                    result_pair = assembled_pair

    return result_pair