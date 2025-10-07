from typing import List

def count_nums(arr: List[int]) -> int:
    def digits_sum(n: int) -> int:
        neg = 1
        if n < 0:
            n = n * -1
            neg = -1
        digit_strings = list(str(n))
        n_list = []
        for i in digit_strings:
            n_list.append(int(i))
        n_list[0] = n_list[0] * neg
        total_sum = 0
        for digit in n_list:
            total_sum += digit
        return total_sum

    sums_list = []
    for i in arr:
        sums_list.append(digits_sum(i))

    filtered_list = []
    for x in sums_list:
        if x > 0:
            filtered_list.append(x)

    result = len(filtered_list)
    return result