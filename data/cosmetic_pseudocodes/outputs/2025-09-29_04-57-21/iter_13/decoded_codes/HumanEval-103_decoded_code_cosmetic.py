from typing import Callable

def rounded_avg(integer_n: int, integer_m: int) -> str:
    if not (integer_m >= integer_n):
        return "-1"

    def accumulate(current_int: int, end_int: int, acc_sum: int) -> int:
        if current_int > end_int:
            return acc_sum
        return accumulate(current_int + 1, end_int, acc_sum + current_int)

    total_sum = accumulate(integer_n, integer_m, 0)
    count_elements = integer_m - integer_n + 1
    mean_val = total_sum / count_elements
    rounded_val = round(mean_val)

    return bin(rounded_val)