from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[float]) -> Optional[Tuple[float, float]]:
    closest_pair: Optional[Tuple[float, float]] = None
    smallest_distance: Optional[float] = None

    for i in range(len(list_of_numbers)):
        current_value = list_of_numbers[i]
        for j in range(len(list_of_numbers)):
            if i != j:
                comparison_value = list_of_numbers[j]
                current_diff = abs(current_value - comparison_value)
                if smallest_distance is None or current_diff < smallest_distance:
                    smallest_distance = current_diff
                    closest_pair = tuple(sorted((current_value, comparison_value)))

    return closest_pair