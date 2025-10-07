from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: Optional[int] = None

    for index1, element1 in enumerate(list_of_numbers):
        for index2, element2 in enumerate(list_of_numbers):
            if index1 != index2:
                dist = abs(element1 - element2)
                if minimum_distance is None or dist < minimum_distance:
                    minimum_distance = dist
                    closest_pair = tuple(sorted((element1, element2)))

    return closest_pair