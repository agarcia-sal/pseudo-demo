from typing import List, Optional


def prod_signs(input_list: List[int]) -> Optional[int]:
    null_result_flag: bool = False
    zero_present_flag: bool = False
    negative_counter: int
    temp_sign: int
    accumulator: int = 0
    current_element: int

    iterator_index: int = 0
    length: int = len(input_list)
    while iterator_index < length:
        current_element = input_list[iterator_index]
        if current_element == 0:
            zero_present_flag = True
        iterator_index += 1

    iterator_index = 0
    while iterator_index < length:
        accumulator += abs(input_list[iterator_index])
        iterator_index += 1

    if length == 0:
        null_result_flag = True

    if null_result_flag:
        return None

    if zero_present_flag:
        temp_sign = 0
    else:
        negative_counter = 0
        iterator_index = 0
        while iterator_index < length:
            current_element = input_list[iterator_index]
            if current_element < 0:
                negative_counter += 1
            iterator_index += 1
        exp_base = -1
        exp_exponent = negative_counter
        temp_sign = 1
        while exp_exponent > 0:
            temp_sign *= exp_base
            exp_exponent -= 1

    return temp_sign * accumulator