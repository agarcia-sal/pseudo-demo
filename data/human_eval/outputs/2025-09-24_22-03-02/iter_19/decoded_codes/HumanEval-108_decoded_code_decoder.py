from typing import List


def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        digits_list = []
        n_str = str(n)
        for index in range(len(n_str)):
            digits_list.append(int(n_str[index]))
        digits_list[0] = digits_list[0] * neg
        digit_sum = 0
        for index in range(len(digits_list)):
            digit_sum += digits_list[index]
        return digit_sum

    digit_sums: List[int] = []
    for index in range(len(arr)):
        digit_sums.append(digits_sum(arr[index]))

    filtered_list: List[int] = []
    for index in range(len(digit_sums)):
        if digit_sums[index] > 0:
            filtered_list.append(digit_sums[index])

    count = len(filtered_list)
    return count