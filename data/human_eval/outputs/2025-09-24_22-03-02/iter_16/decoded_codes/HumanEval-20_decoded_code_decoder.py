from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None

    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            elem2 = numbers[idx2]
            if idx != idx2:
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    sorted_pair = sorted((elem, elem2))
                    closest_pair = (sorted_pair[0], sorted_pair[1])

    return closest_pair