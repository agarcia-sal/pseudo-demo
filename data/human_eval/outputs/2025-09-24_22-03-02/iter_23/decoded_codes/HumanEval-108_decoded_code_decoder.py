from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        digits = []
        str_n = str(n)
        for index in range(len(str_n)):
            digit_char = str_n[index]
            digit_int = int(digit_char)
            digits.append(digit_int)
        digits[0] = digits[0] * neg
        total_sum = 0
        for index in range(len(digits)):
            total_sum += digits[index]
        return total_sum

    filtered_list = []
    for index in range(len(arr)):
        element = arr[index]
        digit_sum_value = digits_sum(element)
        if digit_sum_value > 0:
            filtered_list.append(element)
    result = len(filtered_list)
    return result