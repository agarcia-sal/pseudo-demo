from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    idx = 0
    length = len(numbers)
    while idx < length:
        elem = numbers[idx]
        idx2 = 0
        while idx2 < length:
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    temp_list = []
                    temp_list.append(elem)
                    temp_list.append(elem2)
                    temp_list.sort()
                    closest_pair = (temp_list[0], temp_list[1])
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        temp_list = []
                        temp_list.append(elem)
                        temp_list.append(elem2)
                        temp_list.sort()
                        closest_pair = (temp_list[0], temp_list[1])
            idx2 += 1
        idx += 1
    return closest_pair