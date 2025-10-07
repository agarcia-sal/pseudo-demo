from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None
    for index1, element1 in enumerate(numbers):
        for index2, element2 in enumerate(numbers):
            if index1 != index2:
                if distance is None:
                    distance = abs(element1 - element2)
                    closest_pair = tuple(sorted((element1, element2)))
                else:
                    new_distance = abs(element1 - element2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted((element1, element2)))
    return closest_pair