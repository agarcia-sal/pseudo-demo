from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    dist: Optional[int] = None

    def check_pairs(i: int, j: int) -> None:
        nonlocal closest_pair, dist
        if i >= len(list_of_numbers):
            return
        elif j >= len(list_of_numbers):
            check_pairs(i + 1, 0)
        else:
            val1 = list_of_numbers[i]
            val2 = list_of_numbers[j]
            if i != j:
                diff = abs(val1 - val2)
                if dist is None:
                    dist = diff
                    closest_pair = (val1, val2) if val1 < val2 else (val2, val1)
                elif diff < dist:
                    dist = diff
                    closest_pair = (val1, val2) if val1 < val2 else (val2, val1)
            check_pairs(i, j + 1)

    check_pairs(0, 0)
    return closest_pair