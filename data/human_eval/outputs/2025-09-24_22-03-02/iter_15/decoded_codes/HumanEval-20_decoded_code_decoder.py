from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None
    for idx in range(len(numbers) - 1):
        elem = numbers[idx]
        for idx2 in range(len(numbers) - 1):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    sorted_pair = [elem, elem2]
                    sorted_pair.sort()
                    closest_pair = (sorted_pair[0], sorted_pair[1])
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        sorted_pair = [elem, elem2]
                        sorted_pair.sort()
                        closest_pair = (sorted_pair[0], sorted_pair[1])
    return closest_pair