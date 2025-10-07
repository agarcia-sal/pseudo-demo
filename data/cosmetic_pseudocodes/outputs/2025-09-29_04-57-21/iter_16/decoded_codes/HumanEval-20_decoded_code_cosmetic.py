from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_with_min_distance: Optional[Tuple[int, int]] = None
    min_distance: Optional[int] = None

    for i, current_value in enumerate(list_of_numbers):
        for j, comparison_value in enumerate(list_of_numbers):
            if i != j:
                computed_distance = abs(current_value - comparison_value)
                if min_distance is None or computed_distance < min_distance:
                    min_distance = computed_distance
                    pair_with_min_distance = (min(current_value, comparison_value), max(current_value, comparison_value))

    return pair_with_min_distance