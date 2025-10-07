from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    for index in range(len(list_of_numbers) - 1):
        element = list_of_numbers[index]
        for index2 in range(len(list_of_numbers) - 1):
            element2 = list_of_numbers[index2]
            if index != index2:
                new_distance = abs(element - element2)
                if distance is None or new_distance < distance:
                    distance = new_distance
                    closest_pair = tuple(sorted((element, element2)))

    return closest_pair