from typing import List, Optional


def prod_signs(recv_list: List[int]) -> Optional[int]:
    if len(recv_list) == 0:
        return None

    tmp_flag: bool = False
    idx: int = 0
    while idx < len(recv_list):
        if recv_list[idx] == 0:
            tmp_flag = True
            break
        idx += 1

    if tmp_flag:
        agg_sign: int = 0
    else:
        neg_count: int = 0
        iter_pos: int = 0
        while iter_pos < len(recv_list):
            if recv_list[iter_pos] < 0:
                neg_count += 1
            iter_pos += 1
        tmp_base: int = -1
        power_result: int = 1
        power_idx: int = 0
        while power_idx < neg_count:
            power_result *= tmp_base
            power_idx += 1
        agg_sign = power_result

    total_abs: int = 0
    sum_idx: int = 0
    while sum_idx < len(recv_list):
        val: int = recv_list[sum_idx]
        abs_val: int = -val if val < 0 else val
        total_abs += abs_val
        sum_idx += 1

    final_result: int = agg_sign * total_abs
    return final_result