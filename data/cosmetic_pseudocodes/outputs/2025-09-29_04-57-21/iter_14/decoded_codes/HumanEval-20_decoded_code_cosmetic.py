from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    minimal_diff: Optional[int] = None
    best_match: Optional[Tuple[int, int]] = None

    outer_idx = 0
    length = len(list_of_numbers)
    while outer_idx < length - 1:
        first_val = list_of_numbers[outer_idx]
        inner_idx = 0
        while inner_idx < length - 1:
            second_val = list_of_numbers[inner_idx]
            if outer_idx != inner_idx:
                current_diff = abs(first_val - second_val)
                pair = tuple(sorted((first_val, second_val)))
                if minimal_diff is None or current_diff < minimal_diff:
                    minimal_diff = current_diff
                    best_match = pair
            inner_idx += 1
        outer_idx += 1

    return best_match