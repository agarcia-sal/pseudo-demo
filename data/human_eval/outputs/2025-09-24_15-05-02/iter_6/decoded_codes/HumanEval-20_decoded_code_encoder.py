from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2 = numbers[idx2]
                current_distance = abs(elem - elem2)
                if distance is None or current_distance < distance:
                    distance = current_distance
                    closest_pair = tuple(sorted((elem, elem2)))

    return closest_pair