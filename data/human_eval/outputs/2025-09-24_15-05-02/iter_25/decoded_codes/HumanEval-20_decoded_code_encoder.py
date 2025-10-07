from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None
    n: int = len(list_of_numbers)
    if n < 2:
        return None  # Not enough elements to form a pair
    for idx in range(n):
        elem = list_of_numbers[idx]
        for idx2 in range(n):
            if idx != idx2:
                elem2 = list_of_numbers[idx2]
                diff = abs(elem - elem2)
                if distance is None or diff < distance:
                    distance = diff
                    closest_pair = (min(elem, elem2), max(elem, elem2))
    return closest_pair