from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    length: int = len(numbers)
    for idx in range(length):
        for idx2 in range(length):
            if idx != idx2:
                new_distance: int = abs(numbers[idx] - numbers[idx2])
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted((numbers[idx], numbers[idx2])))
    return closest_pair