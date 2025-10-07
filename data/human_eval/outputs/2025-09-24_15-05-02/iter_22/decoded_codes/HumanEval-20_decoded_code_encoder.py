from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: Optional[int] = None

    length = len(list_of_numbers)
    for index1 in range(length):
        element1 = list_of_numbers[index1]
        for index2 in range(length):
            if index1 != index2:
                element2 = list_of_numbers[index2]
                current_distance = abs(element1 - element2)
                if minimum_distance is None or current_distance < minimum_distance:
                    minimum_distance = current_distance
                    # Store ordered pair with smaller element first
                    if element1 < element2:
                        closest_pair = (element1, element2)
                    else:
                        closest_pair = (element2, element1)
    return closest_pair