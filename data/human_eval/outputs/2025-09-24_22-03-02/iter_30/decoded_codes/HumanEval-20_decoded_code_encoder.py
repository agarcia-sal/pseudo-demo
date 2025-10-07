from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    length = len(numbers)
    idx = 0
    while idx < length:
        elem = numbers[idx]
        idx2 = 0
        while idx2 < length:
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    difference = abs(elem - elem2)
                    distance = difference
                    if elem <= elem2:
                        first_element, second_element = elem, elem2
                    else:
                        first_element, second_element = elem2, elem
                    closest_pair = (first_element, second_element)
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        if elem <= elem2:
                            first_element, second_element = elem, elem2
                        else:
                            first_element, second_element = elem2, elem
                        closest_pair = (first_element, second_element)
            idx2 += 1
        idx += 1
    return closest_pair