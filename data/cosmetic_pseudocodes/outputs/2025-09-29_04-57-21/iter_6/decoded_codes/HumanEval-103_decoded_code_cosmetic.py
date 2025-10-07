from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if integer_m < integer_n:
        return -1
    accumulator: int = 0
    current_index: int = integer_n
    while current_index <= integer_m:
        accumulator += current_index
        current_index += 1
    mean_calc: float = accumulator / (integer_m - integer_n + 1)
    final_result: int = round(mean_calc)
    return bin(final_result)[2:]