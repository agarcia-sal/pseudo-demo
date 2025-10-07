from typing import Optional, Tuple, List


def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted((elem, elem2)))

    return closest_pair