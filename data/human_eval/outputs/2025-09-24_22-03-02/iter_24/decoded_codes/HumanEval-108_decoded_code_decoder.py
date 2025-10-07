from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        digits_list = []
        n_str = str(n)
        index = 0
        while index < len(n_str):
            char = n_str[index]
            digit = int(char)
            digits_list.append(digit)
            index += 1
        digits_list[0] = digits_list[0] * neg
        total_sum = 0
        idx = 0
        while idx < len(digits_list):
            total_sum += digits_list[idx]
            idx += 1
        return total_sum

    sums_list = []
    i = 0
    while i < len(arr):
        sum_value = digits_sum(arr[i])
        sums_list.append(sum_value)
        i += 1

    filtered_list = []
    j = 0
    while j < len(sums_list):
        if sums_list[j] > 0:
            filtered_list.append(sums_list[j])
        j += 1

    result = len(filtered_list)
    return result