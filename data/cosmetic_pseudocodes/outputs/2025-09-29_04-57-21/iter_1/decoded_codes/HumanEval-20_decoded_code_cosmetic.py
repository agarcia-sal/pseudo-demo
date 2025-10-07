from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    min_distance: Optional[int] = None

    length = len(list_of_numbers)
    for i in range(length):
        current_num = list_of_numbers[i]
        for j in range(length):
            if i != j:
                other_num = list_of_numbers[j]
                diff = abs(current_num - other_num)
                if min_distance is None or diff < min_distance:
                    min_distance = diff
                    sorted_pair = sorted([current_num, other_num])
                    closest_pair = (sorted_pair[0], sorted_pair[1])

    return closest_pair