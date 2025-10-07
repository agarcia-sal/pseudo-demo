from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    minimal_gap: Optional[int] = None

    outer_counter = 0
    length = len(list_of_numbers)
    while outer_counter < length - 1:
        current_value = list_of_numbers[outer_counter]
        inner_counter = 0

        while inner_counter < length - 1:
            comparing_value = list_of_numbers[inner_counter]

            if outer_counter != inner_counter:
                gap_candidate = current_value - comparing_value
                if gap_candidate < 0:
                    gap_candidate = -gap_candidate

                if minimal_gap is None or gap_candidate < minimal_gap:
                    minimal_gap = gap_candidate
                    result_pair = (min(current_value, comparing_value), max(current_value, comparing_value))

            inner_counter += 1

        outer_counter += 1

    return result_pair