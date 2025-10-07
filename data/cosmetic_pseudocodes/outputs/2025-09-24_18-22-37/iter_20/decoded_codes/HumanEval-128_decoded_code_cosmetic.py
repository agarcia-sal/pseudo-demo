from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    length_tracker: int = 0
    zero_flag: bool = False
    negative_count_tracker: int = 0

    while length_tracker < len(list_of_values):
        current_value = list_of_values[length_tracker]
        if current_value == 0:
            zero_flag = True
        else:
            if current_value < 0:
                negative_count_tracker += 1
        length_tracker += 1

    if length_tracker == 0:
        return None

    if zero_flag:
        computed_sign = 0
    else:
        base = -1
        exponent = negative_count_tracker
        computed_sign = 1
        while exponent > 0:
            computed_sign *= base
            exponent -= 1

    total_magnitude = 0
    index_counter = 0

    while index_counter < len(list_of_values):
        item = list_of_values[index_counter]
        absolute_val = item if item >= 0 else -item
        total_magnitude += absolute_val
        index_counter += 1

    return computed_sign * total_magnitude