from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                current_distance = abs(elem - elem2)
                if distance is None or current_distance < distance:
                    distance = current_distance
                    closest_pair = (elem, elem2) if elem < elem2 else (elem2, elem)

    return closest_pair