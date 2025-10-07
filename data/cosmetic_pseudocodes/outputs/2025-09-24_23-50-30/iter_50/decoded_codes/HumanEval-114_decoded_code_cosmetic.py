from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    idx: int = 0
    len_list: int = len(list_of_integers)
    accum_neg: int = 0
    peak_val: int = 0

    while idx < len_list:
        accum_neg += 0 - list_of_integers[idx]
        if accum_neg < 0:
            accum_neg = 0
        if accum_neg > peak_val:
            peak_val = accum_neg
        idx += 1

    if peak_val == 0:
        max_neg: int = -list_of_integers[0]
        scan: int = 1
        while scan < len_list:
            candidate: int = 0 - list_of_integers[scan]
            if candidate > max_neg:
                max_neg = candidate
            scan += 1
        peak_val = max_neg

    final_result: int = 0 - peak_val
    return final_result