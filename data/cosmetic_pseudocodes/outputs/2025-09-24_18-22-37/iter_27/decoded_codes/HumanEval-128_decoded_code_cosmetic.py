from typing import List, Optional


def prod_signs(mixed_list: List[int]) -> Optional[int]:
    if len(mixed_list) == 0:
        return None

    zero_found_flag: bool = False
    neg_count: int = 0
    idx: int = 0

    while idx < len(mixed_list):
        curr_val = mixed_list[idx]
        if curr_val == 0:
            zero_found_flag = True
        elif curr_val < 0:
            neg_count += 1
        idx += 1

    result_sign: int = 0
    if zero_found_flag:
        result_sign = 0
    else:
        powered_val = 1
        power_base = -1
        power_exp = neg_count
        while power_exp > 0:
            powered_val *= power_base
            power_exp -= 1
        result_sign = powered_val

    total_abs: int = 0
    idx2: int = 0
    while idx2 < len(mixed_list):
        abs_curr = mixed_list[idx2]
        if abs_curr < 0:
            abs_curr = -abs_curr
        total_abs += abs_curr
        idx2 += 1

    return result_sign * total_abs