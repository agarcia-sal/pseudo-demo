from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_candidate: Optional[Tuple[int, int]] = None
    minimal_gap: Optional[int] = None

    outer_pos = 0
    n = len(list_of_numbers)
    while outer_pos < n - 1:
        first_value = list_of_numbers[outer_pos]

        inner_pos = 0
        while inner_pos < n:
            if outer_pos != inner_pos:
                second_value = list_of_numbers[inner_pos]
                gap = abs(first_value - second_value)
                if minimal_gap is None or gap < minimal_gap:
                    minimal_gap = gap
                    pair_candidate = (min(first_value, second_value), max(first_value, second_value))
            inner_pos += 1

        outer_pos += 1

    return pair_candidate