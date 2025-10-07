from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None

    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            elem2 = numbers[idx2]
            if idx != idx2:
                current_distance = abs(elem - elem2)
                if distance is None or current_distance < distance:
                    distance = current_distance
                    closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair