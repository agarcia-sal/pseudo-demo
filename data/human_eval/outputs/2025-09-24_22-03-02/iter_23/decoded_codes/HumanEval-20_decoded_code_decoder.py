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
                difference = elem - elem2
                if difference < 0:
                    difference = -difference
                if distance is None:
                    distance = difference
                    if elem <= elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)
                else:
                    new_distance = difference
                    if new_distance < distance:
                        distance = new_distance
                        if elem <= elem2:
                            closest_pair = (elem, elem2)
                        else:
                            closest_pair = (elem2, elem)
    return closest_pair