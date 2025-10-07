from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    closest_pair: Optional[Tuple[int, int]] = None
    minimum_distance: Optional[int] = None
    length = len(list_of_numbers)

    def recurse(i: int) -> None:
        nonlocal closest_pair, minimum_distance
        if i < 0:
            return

        def inner_recurse(j: int) -> None:
            nonlocal closest_pair, minimum_distance
            if j < 0:
                return
            if i != j:
                current_distance = abs(list_of_numbers[i] - list_of_numbers[j])
                if minimum_distance is None or current_distance < minimum_distance:
                    minimum_distance = current_distance
                    pair = (list_of_numbers[i], list_of_numbers[j])
                    if pair[0] > pair[1]:
                        pair = (pair[1], pair[0])
                    closest_pair = pair
            inner_recurse(j - 1)

        inner_recurse(length - 1)
        recurse(i - 1)

    recurse(length - 1)
    return closest_pair