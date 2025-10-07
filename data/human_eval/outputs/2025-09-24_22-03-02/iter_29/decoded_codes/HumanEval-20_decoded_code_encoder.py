from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    length_numbers = len(numbers)
    for idx in range(length_numbers):
        elem = numbers[idx]
        for idx2 in range(length_numbers):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    temp_list = [elem, elem2]
                    temp_list.sort()
                    closest_pair = (temp_list[0], temp_list[1])
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        temp_list = [elem, elem2]
                        temp_list.sort()
                        closest_pair = (temp_list[0], temp_list[1])
    return closest_pair