from typing import List, Optional


def minSubArraySum(arr_nums: List[int]) -> int:
    acc_max: int = 0
    acc_tmp: int = 0

    def recur_idx(idx: int) -> None:
        nonlocal acc_max, acc_tmp
        if idx >= len(arr_nums):
            return
        acc_tmp += -arr_nums[idx]
        if acc_tmp < 0:
            acc_tmp = 0
        if acc_tmp > acc_max:
            acc_max = acc_tmp
        recur_idx(idx + 1)

    recur_idx(0)

    if acc_max == 0:
        inverted_values = [-val for val in arr_nums]
        acc_max = inverted_values[0]
        for val in inverted_values[1:]:
            if val > acc_max:
                acc_max = val

    result_minimum: int = -acc_max
    return result_minimum