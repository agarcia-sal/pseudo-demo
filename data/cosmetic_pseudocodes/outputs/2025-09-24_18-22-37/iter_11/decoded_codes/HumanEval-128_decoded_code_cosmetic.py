from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    idx: int = 0
    length_array: int = len(array_of_integers)

    if length_array == 0:
        return None

    zero_found: bool = False
    while idx < length_array and not zero_found:
        if array_of_integers[idx] == 0:
            zero_found = True
        idx += 1

    if zero_found:
        sign_product: int = 0
    else:
        neg_count: int = 0
        inner_idx: int = 0
        while inner_idx < length_array:
            current_value: int = array_of_integers[inner_idx]
            if current_value < 0:
                neg_count += 1
            inner_idx += 1

        base_val: int = -1
        exponent_val: int = neg_count
        temp_result: int = 1
        exp_counter: int = 0

        while exp_counter < exponent_val:
            temp_result *= base_val
            exp_counter += 1

        sign_product = temp_result

    total_sum: int = 0
    sum_idx: int = 0
    while sum_idx < length_array:
        elem_abs: int = array_of_integers[sum_idx]
        if elem_abs < 0:
            elem_abs = -elem_abs
        total_sum += elem_abs
        sum_idx += 1

    final_result: int = sign_product * total_sum
    return final_result