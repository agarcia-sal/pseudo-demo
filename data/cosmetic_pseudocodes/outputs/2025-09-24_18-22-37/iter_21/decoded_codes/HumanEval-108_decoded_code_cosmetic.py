from typing import List


def count_nums(input_array: List[int]) -> int:
    def digits_sum(num: int) -> int:
        multiplier = 1
        while num < 0:
            num = -num
            multiplier = -1

        digits_str = str(num)
        digits_arr: List[int] = []
        idx = 0

        while idx < len(digits_str):
            ch = digits_str[idx]
            digit_val = int(ch)
            digits_arr.append(digit_val)
            idx += 1

        first_digit = digits_arr[0]
        first_digit *= multiplier
        digits_arr[0] = first_digit

        total = 0
        for val in digits_arr:
            total += val

        return total

    digit_sums_list: List[int] = []

    i = 0
    while i < len(input_array):
        val = input_array[i]
        sum_val = digits_sum(val)
        digit_sums_list.append(sum_val)
        i += 1

    positive_only: List[int] = []
    for s in digit_sums_list:
        if s > 0:
            positive_only.append(s)

    return len(positive_only)