from typing import List


def minSubArraySum(array_of_numbers: List[int]) -> int:
    agg_flag: int | bool = False
    cursor_value: int = 0
    index_pointer: int = 0
    length: int = len(array_of_numbers)

    while index_pointer < length:
        current_val: int = array_of_numbers[index_pointer]
        negated_val: int = 0 - current_val
        cursor_value += negated_val
        if not (cursor_value >= 0):
            cursor_value = 0
        if agg_flag is False or cursor_value > agg_flag:
            agg_flag = cursor_value
        index_pointer += 1

    if agg_flag == 0:
        candidates: List[int] = []
        pos_idx: int = 0
        while pos_idx < length:
            element_neg: int = 0 - array_of_numbers[pos_idx]
            candidates.append(element_neg)
            pos_idx += 1

        top_val: int = candidates[0]
        search_idx: int = 1
        while search_idx < len(candidates):
            if candidates[search_idx] > top_val:
                top_val = candidates[search_idx]
            search_idx += 1
        agg_flag = top_val

    final_result: int = 0 - agg_flag
    return final_result