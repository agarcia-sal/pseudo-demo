from typing import List


def add_elements(list_nums: List[int], count_n: int) -> int:
    acc_total: int = 0
    index_i: int = 0
    while index_i < count_n:
        current_val: int = list_nums[index_i]
        if len(str(current_val)) <= 2:
            acc_total += current_val
        index_i += 1
    return acc_total