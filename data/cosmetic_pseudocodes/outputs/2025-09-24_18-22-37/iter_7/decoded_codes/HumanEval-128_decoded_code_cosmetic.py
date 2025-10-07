from typing import List, Optional

def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None

    zero_found: bool = False
    idx: int = 0
    length: int = len(list_of_values)
    while idx < length:
        if list_of_values[idx] == 0:
            zero_found = True
            break
        idx += 1

    if zero_found:
        sign_result: int = 0
    else:
        neg_count: int = 0
        idx = 0
        while idx < length:
            if list_of_values[idx] < 0:
                neg_count += 1
            idx += 1
        sign_base: int = -1
        power_result: int = 1
        exp_counter: int = 0
        while exp_counter < neg_count:
            power_result *= sign_base
            exp_counter += 1
        sign_result = power_result

    total_magnitude: int = 0
    idx = 0
    while idx < length:
        current_val: int = list_of_values[idx]
        if current_val < 0:
            current_val = -current_val
        total_magnitude += current_val
        idx += 1

    final_result: int = sign_result * total_magnitude
    return final_result