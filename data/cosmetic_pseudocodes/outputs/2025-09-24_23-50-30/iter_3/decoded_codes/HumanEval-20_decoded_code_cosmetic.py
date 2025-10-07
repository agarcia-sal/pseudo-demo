from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_min: Optional[int] = None

    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if i != j:
                diff = list_of_numbers[i] - list_of_numbers[j]
                abs_diff = diff if diff >= 0 else -diff
                if dist_min is None or abs_diff < dist_min:
                    dist_min = abs_diff
                    if list_of_numbers[i] < list_of_numbers[j]:
                        pair_closest = (list_of_numbers[i], list_of_numbers[j])
                    else:
                        pair_closest = (list_of_numbers[j], list_of_numbers[i])
    return pair_closest