from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: float = float("inf")

    length: int = len(list_of_numbers)
    for i in range(length - 1):
        element1: int = list_of_numbers[i]
        j: int = i + 1
        while j < length:
            element2: int = list_of_numbers[j]
            current_distance: int = abs(element1 - element2)
            if current_distance < minimum_distance:
                minimum_distance = current_distance
                if element1 < element2:
                    closest_pair = (element1, element2)
                else:
                    closest_pair = (element2, element1)
            j += 1

    return closest_pair