from typing import List, Optional

def find_closest_elements(numbers: List[int]) -> Optional[List[int]]:
    closest_pair: Optional[List[int]] = None
    distance: Optional[int] = None
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            elem2 = numbers[idx2]
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    if elem < elem2:
                        closest_pair = [elem, elem2]
                    else:
                        closest_pair = [elem2, elem]
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        if elem < elem2:
                            closest_pair = [elem, elem2]
                        else:
                            closest_pair = [elem2, elem]
    return closest_pair