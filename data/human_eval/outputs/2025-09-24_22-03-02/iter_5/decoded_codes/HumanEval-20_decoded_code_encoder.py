from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None

    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            if idx != idx2:
                elem2 = numbers[idx2]
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = (min(elem, elem2), max(elem, elem2))

    return closest_pair