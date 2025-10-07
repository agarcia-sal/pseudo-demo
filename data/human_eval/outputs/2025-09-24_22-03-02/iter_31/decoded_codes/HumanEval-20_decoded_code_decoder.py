from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None

    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            if idx != idx2:
                elem2 = numbers[idx2]
                diff = abs(elem - elem2)
                if distance is None or diff < distance:
                    distance = diff
                    if elem < elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)

    return closest_pair