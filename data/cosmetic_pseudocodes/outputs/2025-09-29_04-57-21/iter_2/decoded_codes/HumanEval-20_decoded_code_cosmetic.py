from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    min_diff: Optional[int] = None

    for i, val1 in enumerate(list_of_numbers):
        for j, val2 in enumerate(list_of_numbers):
            if i != j:
                current_diff = abs(val1 - val2)

                if min_diff is None or current_diff < min_diff:
                    min_diff = current_diff
                    result_pair = (val1, val2) if val1 < val2 else (val2, val1)

    return result_pair