from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None
    n = len(numbers)
    for idx in range(n):
        elem = numbers[idx]
        for idx2 in range(n):
            if idx != idx2:
                elem2 = numbers[idx2]
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted((elem, elem2)))
    return closest_pair