from typing import List, Optional, Tuple


def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    least_diff: Optional[int] = None

    for posA, valA in enumerate(array_of_values):
        for posB, valB in enumerate(array_of_values):
            if posA != posB:
                current_diff = abs(valA - valB)
                if least_diff is None or current_diff < least_diff:
                    least_diff = current_diff
                    pair_result = (min(valA, valB), max(valA, valB))

    return pair_result