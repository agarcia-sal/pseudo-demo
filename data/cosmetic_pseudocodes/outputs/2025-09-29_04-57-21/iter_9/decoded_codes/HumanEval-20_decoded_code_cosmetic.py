from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_with_min_gap: Optional[Tuple[int, int]] = None
    minimum_gap: Optional[int] = None

    outer_index: int = 0
    length: int = len(list_of_numbers)
    while outer_index < length - 1:
        first_value: int = list_of_numbers[outer_index]
        inner_index: int = 0

        while inner_index < length - 1:
            second_value: int = list_of_numbers[inner_index]

            if outer_index != inner_index:
                current_gap = abs(second_value - first_value)
                if minimum_gap is not None:
                    if current_gap < minimum_gap:
                        minimum_gap = current_gap
                        sorted_values = sorted([first_value, second_value])
                        pair_with_min_gap = (sorted_values[0], sorted_values[1])
                else:
                    minimum_gap = current_gap
                    values_sorted = sorted([second_value, first_value])
                    pair_with_min_gap = (values_sorted[0], values_sorted[1])

            inner_index += 1

        outer_index += 1

    return pair_with_min_gap