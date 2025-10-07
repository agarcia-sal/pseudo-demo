from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if not (integer_m >= integer_n):
        return -1
    total_sum: int = 0
    current_index: int = integer_n
    while current_index <= integer_m:
        total_sum += current_index
        current_index += 1
    count_of_numbers: int = (integer_m - integer_n) + 1
    raw_average: float = total_sum / count_of_numbers
    nearest_int: int = int(raw_average + 0.5)  # rounding to nearest int
    return bin(nearest_int)