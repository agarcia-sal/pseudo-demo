from typing import List

def prod_signs(list_of_nums: List[int]) -> int:
    if not list_of_nums:
        return 0  # if empty, product magnitude is zero

    if 0 in list_of_nums:
        result_sign = 0
    else:
        negative_counter = 0
        index_var = 0
        while index_var < len(list_of_nums):
            if list_of_nums[index_var] < 0:
                negative_counter += 1
            index_var += 1
        result_sign = 1
        neg_index = negative_counter
        while neg_index > 0:
            result_sign = -1 * result_sign
            neg_index -= 1

    magnitude_sum = 0
    pos = 0
    while pos < len(list_of_nums):
        val = list_of_nums[pos]
        magnitude_sum += val if val >= 0 else -val
        pos += 1

    return result_sign * magnitude_sum