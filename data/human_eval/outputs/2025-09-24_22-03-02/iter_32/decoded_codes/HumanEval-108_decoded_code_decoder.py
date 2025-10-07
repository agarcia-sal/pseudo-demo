from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        str_n = str(n)
        digit_list = []
        for index in range(len(str_n)):
            char = str_n[index]
            digit = int(char)
            digit_list.append(digit)
        digit_at_zero = digit_list[0]
        digit_at_zero = digit_at_zero * neg
        digit_list[0] = digit_at_zero
        total_sum = 0
        for index in range(len(digit_list)):
            total_sum += digit_list[index]
        return total_sum

    digit_sums = []
    for index in range(len(arr)):
        element = arr[index]
        sum_value = digits_sum(n=element)
        digit_sums.append(sum_value)
    count = 0
    for index in range(len(digit_sums)):
        value = digit_sums[index]
        if value > 0:
            count += 1
    return count