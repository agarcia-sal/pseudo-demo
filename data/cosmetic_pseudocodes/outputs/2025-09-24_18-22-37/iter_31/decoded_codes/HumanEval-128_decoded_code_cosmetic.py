from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if len(list_of_values) == 0:
        return None

    zero_found_flag = False
    for each_element in list_of_values:
        if each_element == 0:
            zero_found_flag = True
            break

    if zero_found_flag:
        sign_result = 0
    else:
        neg_count = sum(1 for v in list_of_values if v < 0)
        power_base = -1
        power_exp = neg_count
        temp_sign = 1
        while power_exp > 0:
            temp_sign *= power_base
            power_exp -= 1
        sign_result = temp_sign

    total_magnitude = 0
    for position in range(len(list_of_values)):
        current_abs = list_of_values[position]
        if current_abs < 0:
            current_abs = -current_abs
        total_magnitude += current_abs

    output_value = sign_result * total_magnitude
    return output_value