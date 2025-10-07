from typing import Optional


def rounded_avg(integer_n: int, integer_m: int) -> Optional[str]:
    if integer_m < integer_n:
        return -1
    total_sum: int = 0
    current_num: int = integer_n
    while current_num <= integer_m:
        total_sum += current_num
        current_num += 1
    count: int = integer_m - integer_n + 1
    mean_value: float = total_sum / count
    rounded_result: int = round(mean_value)
    return bin(rounded_result)