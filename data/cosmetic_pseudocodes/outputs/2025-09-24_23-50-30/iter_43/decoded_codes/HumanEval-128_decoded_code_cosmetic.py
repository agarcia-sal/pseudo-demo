from typing import List, Optional


def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    if len(list_of_numbers) == 0:
        return None

    # Check for zero in list, if any zero found, result_sign = 0
    for num in list_of_numbers:
        if num == 0:
            result_sign = 0
            break
    else:
        # Count negative numbers if no zero found
        neg_count = 0
        index_counter = 0
        while index_counter < len(list_of_numbers):
            if list_of_numbers[index_counter] < 0:
                neg_count += 1
            index_counter += 1

        result_sign = 1
        temp_power = neg_count
        while temp_power > 0:
            result_sign *= -1
            temp_power -= 1

    aggregate_abs_sum = 0
    for num in list_of_numbers:
        aggregate_abs_sum += -num if num < 0 else num

    return result_sign * aggregate_abs_sum