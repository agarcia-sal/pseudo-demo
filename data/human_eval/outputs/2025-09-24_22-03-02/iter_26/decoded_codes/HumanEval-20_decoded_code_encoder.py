from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2 = numbers[idx2]
                if distance is None:
                    distance = abs(elem - elem2)
                    smaller, larger = (elem, elem2) if elem <= elem2 else (elem2, elem)
                    closest_pair = (smaller, larger)
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        smaller, larger = (elem, elem2) if elem <= elem2 else (elem2, elem)
                        closest_pair = (smaller, larger)
    return closest_pair