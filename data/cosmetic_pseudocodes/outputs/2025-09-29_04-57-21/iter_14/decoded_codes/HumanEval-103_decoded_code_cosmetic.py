from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"
    accumulator = 0
    iterator = integer_n
    while iterator <= integer_m:
        accumulator += iterator
        iterator += 1
    count_elements = integer_m - integer_n + 1
    mean_val = accumulator / count_elements
    final_rounded = round(mean_val)
    return bin(final_rounded)