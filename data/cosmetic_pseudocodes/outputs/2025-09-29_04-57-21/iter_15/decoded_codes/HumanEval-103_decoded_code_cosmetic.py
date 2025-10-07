from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if integer_n > integer_m:
        return -1
    total_sum: int = 0
    current_number: int = integer_n
    while current_number <= integer_m:
        total_sum += current_number
        current_number += 1
    count_of_numbers: int = (integer_m + 1) - integer_n
    raw_avg: float = total_sum / count_of_numbers
    nearest_int: int = int(raw_avg + 0.5)  # round half up (towards +inf)
    return bin(nearest_int)