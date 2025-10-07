from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None

    for index1, element1 in enumerate(numbers):
        for index2, element2 in enumerate(numbers):
            if index1 != index2:
                new_distance = abs(element1 - element2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted((element1, element2)))

    return closest_pair