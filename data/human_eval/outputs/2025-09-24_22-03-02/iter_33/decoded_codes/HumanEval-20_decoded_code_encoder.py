from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None
    length_numbers = len(numbers)

    for idx in range(length_numbers):
        elem = numbers[idx]
        for idx2 in range(length_numbers):
            if idx != idx2:
                elem2 = numbers[idx2]
                difference = abs(elem - elem2)
                if distance is None or difference < distance:
                    distance = difference
                    if elem < elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)
    return closest_pair