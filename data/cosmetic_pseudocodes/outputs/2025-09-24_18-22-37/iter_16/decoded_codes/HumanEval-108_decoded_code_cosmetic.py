from typing import List

def count_nums(arr_of_ints: List[int]) -> int:
    def digits_sum(param_num: int) -> int:
        multiplier_sign = 1
        if param_num < 0:
            param_num = -param_num
            multiplier_sign = -1
        str_digits = str(param_num)
        digit_list: List[int] = []
        idx = 0
        while idx < len(str_digits):
            digit_list.append(int(str_digits[idx]))
            idx += 1
        digit_list[0] *= multiplier_sign
        total_sum = 0
        i = 0
        while i < len(digit_list):
            total_sum += digit_list[i]
            i += 1
        return total_sum

    accum_sums: List[int] = []
    j = 0
    while j < len(arr_of_ints):
        elem = arr_of_ints[j]
        val = digits_sum(elem)
        accum_sums.append(val)
        j += 1

    pos_filtered: List[int] = []
    k = 0
    while k < len(accum_sums):
        candidate = accum_sums[k]
        if candidate > 0:
            pos_filtered.append(candidate)
        k += 1

    return len(pos_filtered)