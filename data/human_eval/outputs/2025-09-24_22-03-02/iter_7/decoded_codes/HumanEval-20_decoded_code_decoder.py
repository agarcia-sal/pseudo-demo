from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None

    n = len(numbers)
    for idx in range(n):
        elem = numbers[idx]
        for idx2 in range(n):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = (min(elem, elem2), max(elem, elem2))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = (min(elem, elem2), max(elem, elem2))

    return closest_pair  # type: ignore