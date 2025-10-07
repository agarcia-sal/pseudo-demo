from typing import List


def count_nums(nums_array: List[int]) -> int:
    def digits_sum(num: int) -> int:
        multiplier = 1
        if num < 0:
            num = -num
            multiplier = -1
        digits_str = str(num)
        digits_arr: List[int] = []
        idx = 0
        while idx < len(digits_str):
            digits_arr.append(int(digits_str[idx]))
            idx += 1
        digits_arr[0] *= multiplier  # Apply sign to most significant digit
        total = 0
        j = 0
        while j < len(digits_arr):
            total += digits_arr[j]
            j += 1
        return total

    sums_list: List[int] = []
    i = 0
    while i < len(nums_array):
        sums_list.append(digits_sum(nums_array[i]))
        i += 1

    positives: List[int] = []
    k = 0
    while k < len(sums_list):
        # switch true: if sums_list[k] > 0 then append
        if sums_list[k] > 0:
            positives.append(sums_list[k])
        k += 1

    return len(positives)