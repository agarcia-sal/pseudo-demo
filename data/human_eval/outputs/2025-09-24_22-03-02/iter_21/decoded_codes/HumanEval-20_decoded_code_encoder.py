from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    idx = 0
    while idx < len(numbers):
        elem = numbers[idx]
        idx2 = 0
        while idx2 < len(numbers):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    sorted_temp_list = sorted([elem, elem2])
                    closest_pair = (sorted_temp_list[0], sorted_temp_list[1])
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        sorted_temp_list = sorted([elem, elem2])
                        closest_pair = (sorted_temp_list[0], sorted_temp_list[1])
            idx2 += 1
        idx += 1
    return closest_pair