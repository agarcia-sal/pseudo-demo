from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    distance: Optional[int] = None

    length = len(list_of_numbers)
    if length < 2:
        return None

    for index_one, element_one in enumerate(list_of_numbers):
        for index_two, element_two in enumerate(list_of_numbers):
            if index_one != index_two:
                diff = abs(element_one - element_two)
                if distance is None or diff < distance:
                    distance = diff
                    closest_pair = tuple(sorted((element_one, element_two)))

    return closest_pair