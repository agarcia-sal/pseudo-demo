from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if not (integer_m >= integer_n):
        return -1
    accumulator = 0
    iterator = integer_n
    while iterator <= integer_m:
        accumulator += iterator
        iterator += 1
    count = (integer_m - integer_n) + 1
    mean_val = accumulator / count
    final_result = round(mean_val)
    return bin(final_result)