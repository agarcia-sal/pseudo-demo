from typing import List, Tuple, Optional

def find_closest_elements(numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair = None
    distance = None
    index_i = 0
    while index_i < len(numbers):
        elem = numbers[index_i]
        index_j = 0
        while index_j < len(numbers):
            elem2 = numbers[index_j]
            if index_i != index_j:
                if distance is None:
                    distance = abs(elem - elem2)
                    if elem <= elem2:
                        closest_pair = (elem, elem2)
                    else:
                        closest_pair = (elem2, elem)
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        if elem <= elem2:
                            closest_pair = (elem, elem2)
                        else:
                            closest_pair = (elem2, elem)
            index_j += 1
        index_i += 1
    return closest_pair