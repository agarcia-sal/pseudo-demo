from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None

    idx = 0
    length = len(numbers)
    while idx < length:
        elem = numbers[idx]
        idx2 = 0
        while idx2 < length:
            elem2 = numbers[idx2]
            if idx != idx2:
                difference = elem - elem2
                if difference < 0:
                    difference = -difference
                if distance is None:
                    distance = difference
                    if elem < elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)
                else:
                    new_distance = difference
                    if new_distance < distance:
                        distance = new_distance
                        if elem < elem2:
                            closest_pair = (elem, elem2)
                        else:
                            closest_pair = (elem2, elem)
            idx2 += 1
        idx += 1

    return closest_pair