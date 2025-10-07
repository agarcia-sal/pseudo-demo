from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None

    zero_found_flag: bool = False
    index_var: int = 0
    while index_var < len(list_of_values) and not zero_found_flag:
        if list_of_values[index_var] == 0:
            zero_found_flag = True
        index_var += 1

    if zero_found_flag:
        intermediate_sign: int = 0
    else:
        negative_counter: int = 0
        ptr_var: int = 0
        while ptr_var < len(list_of_values):
            if list_of_values[ptr_var] < 0:
                negative_counter += 1
            ptr_var += 1
        intermediate_sign = 1
        for _ in range(negative_counter):
            intermediate_sign *= -1

    running_sum: int = 0
    iter_var: int = 0
    while iter_var < len(list_of_values):
        temp_abs = list_of_values[iter_var]
        if temp_abs < 0:
            temp_abs = -temp_abs
        running_sum += temp_abs
        iter_var += 1

    return intermediate_sign * running_sum