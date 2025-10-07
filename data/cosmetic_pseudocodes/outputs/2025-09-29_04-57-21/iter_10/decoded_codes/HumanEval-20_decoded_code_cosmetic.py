from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    best_pair: Optional[Tuple[int, int]] = None
    min_diff: Optional[int] = None

    i: int = 0
    length: int = len(list_of_numbers)
    while i < length:
        val1: int = list_of_numbers[i]

        j: int = 0
        while j < length:
            val2: int = list_of_numbers[j]

            if i == j:
                j += 1
                continue

            curr_diff: int = val1 - val2
            if curr_diff < 0:
                curr_diff = -curr_diff

            if min_diff is None:
                min_diff = curr_diff
                best_pair = (val1, val2) if val1 <= val2 else (val2, val1)
            elif curr_diff < min_diff:
                min_diff = curr_diff
                best_pair = (val1, val2) if val1 <= val2 else (val2, val1)

            j += 1

        i += 1

    return best_pair