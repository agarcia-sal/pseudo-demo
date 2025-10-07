from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2 = numbers[idx2]
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))
    return closest_pair