from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_found: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for first_index in range(len(list_of_numbers)):
        for second_index in range(len(list_of_numbers)):
            if first_index != second_index:
                current_difference = abs(list_of_numbers[first_index] - list_of_numbers[second_index])

                if smallest_gap is None or current_difference < smallest_gap:
                    smallest_gap = current_difference
                    a, b = list_of_numbers[first_index], list_of_numbers[second_index]
                    pair_found = (a, b) if a <= b else (b, a)

    return pair_found