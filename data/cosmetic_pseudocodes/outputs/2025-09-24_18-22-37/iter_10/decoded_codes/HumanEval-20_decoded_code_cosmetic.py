from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    interim_min_dist: Optional[int] = None
    interim_closest: Optional[Tuple[int, int]] = None

    for outer_counter, outer_value in enumerate(list_of_numbers):
        for inner_counter, inner_value in enumerate(list_of_numbers):
            if outer_counter != inner_counter:
                computed_distance = abs(outer_value - inner_value)
                if interim_min_dist is None or computed_distance < interim_min_dist:
                    interim_min_dist = computed_distance
                    interim_closest = tuple(sorted((outer_value, inner_value)))

    return interim_closest