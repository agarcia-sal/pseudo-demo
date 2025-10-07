from typing import Union

def rounded_avg(integer_n: int, integer_m: int) -> str:
    def recursive_add(current: int, end: int) -> int:
        if current > end:
            return 0
        return current + recursive_add(current + 1, end)

    if integer_m < integer_n:
        return "-1"

    integer_sum: int = recursive_add(integer_n, integer_m)
    integer_length: int = (integer_m - integer_n) + 1
    average_val: float = integer_sum / integer_length
    rounded_val: int = round(average_val)

    return bin(rounded_val)[2:]