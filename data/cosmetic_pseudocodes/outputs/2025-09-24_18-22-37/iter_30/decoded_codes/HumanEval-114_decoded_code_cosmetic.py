from typing import List

def minSubArraySum(passed_array: List[int]) -> int:
    acc_total: int = 0
    max_accum: int = 0
    idx: int = 0

    while idx < len(passed_array):
        cur_val = passed_array[idx]
        acc_total += 0 - cur_val  # accumulate negated values
        if acc_total < 0:
            acc_total = 0
        if max_accum < acc_total:
            max_accum = acc_total
        idx += 1

    if max_accum == 0:
        inverted_values = [-val for val in passed_array]
        max_of_inverted = inverted_values[0]
        for ele in inverted_values:
            if ele > max_of_inverted:
                max_of_inverted = ele
        max_accum = max_of_inverted

    result_sum = 0 - max_accum
    return result_sum