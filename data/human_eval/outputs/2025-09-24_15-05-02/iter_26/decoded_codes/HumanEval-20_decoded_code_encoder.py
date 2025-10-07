from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    n = len(list_of_numbers)
    for index1 in range(n):
        element1 = list_of_numbers[index1]
        for index2 in range(n):
            if index1 != index2:
                element2 = list_of_numbers[index2]
                new_distance = abs(element1 - element2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    # tuple with smaller element first
                    closest_pair = (element1, element2) if element1 < element2 else (element2, element1)

    return closest_pair