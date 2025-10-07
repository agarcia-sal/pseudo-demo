from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    distance: Optional[float] = None
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2 = numbers[idx2]
                new_distance = abs(elem - elem2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    temp_list = sorted([elem, elem2])
                    closest_pair = (temp_list[0], temp_list[1])
    return closest_pair