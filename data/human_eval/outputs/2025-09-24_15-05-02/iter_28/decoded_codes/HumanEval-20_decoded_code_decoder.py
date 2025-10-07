from typing import Optional, Tuple, List

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    length = len(numbers)
    if length < 2:
        return None

    for index1 in range(length):
        elem1 = numbers[index1]
        for index2 in range(length):
            if index1 == index2:
                continue
            elem2 = numbers[index2]
            new_distance = abs(elem1 - elem2)
            if distance is None or new_distance < distance:
                distance = new_distance
                closest_pair = tuple(sorted((elem1, elem2)))

    return closest_pair