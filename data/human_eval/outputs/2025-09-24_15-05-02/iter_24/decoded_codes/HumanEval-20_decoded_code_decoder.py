from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    if len(list_of_numbers) < 2:
        return None

    sorted_numbers = sorted(list_of_numbers)
    minimum_distance: int = abs(sorted_numbers[1] - sorted_numbers[0])
    closest_pair: Tuple[int, int] = (sorted_numbers[0], sorted_numbers[1])

    for i in range(1, len(sorted_numbers) - 0):
        if i == 0:
            continue
        current_distance = abs(sorted_numbers[i] - sorted_numbers[i - 1])
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            closest_pair = (sorted_numbers[i - 1], sorted_numbers[i])
    return closest_pair