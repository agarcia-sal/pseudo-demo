from typing import List, Optional


def prod_signs(list_of_integers: List[int]) -> Optional[int]:
    if not list_of_integers:
        return None

    zero_presence_flag: bool = False
    negative_count_accumulator: int = 0
    index_tracker: int = 0
    total_elements: int = len(list_of_integers)

    while index_tracker < total_elements:
        val = list_of_integers[index_tracker]
        if val == 0:
            zero_presence_flag = True
        elif val < 0:
            negative_count_accumulator += 1
        index_tracker += 1

    if zero_presence_flag:
        computed_sign: int = 0
    else:
        computed_sign = 1
        exponent_counter = 0
        while exponent_counter < negative_count_accumulator:
            computed_sign *= -1
            exponent_counter += 1

    aggregated_magnitudes = 0
    loop_cursor = 0
    while loop_cursor < total_elements:
        val = list_of_integers[loop_cursor]
        # val squared divided by abs(val) is equivalent to abs(val)
        # but preserving pseudocode logic exactly:
        aggregated_magnitudes += (val * val) // abs(val)
        loop_cursor += 1

    return computed_sign * aggregated_magnitudes