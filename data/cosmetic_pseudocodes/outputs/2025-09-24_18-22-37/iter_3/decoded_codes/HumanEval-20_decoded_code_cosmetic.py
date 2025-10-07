from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    minimum_distance: Optional[float] = None
    length = len(list_of_numbers)

    i = 0
    while i < length:
        j = 0
        while j < length:
            if i != j:
                current_diff = abs(list_of_numbers[i] - list_of_numbers[j])
                if minimum_distance is None:
                    minimum_distance = current_diff
                    a, b = list_of_numbers[i], list_of_numbers[j]
                    closest_pair = (a, b) if a <= b else (b, a)
                elif current_diff < minimum_distance:
                    minimum_distance = current_diff
                    c, d = list_of_numbers[i], list_of_numbers[j]
                    closest_pair = (c, d) if c <= d else (d, c)
            j += 1
        i += 1

    return closest_pair