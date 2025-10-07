from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    if not (integer_m >= integer_n):
        return -1
    total_sum: int = 0
    current_num: int = integer_n
    while current_num <= integer_m:
        total_sum += current_num
        current_num += 1
    count_elements: int = (integer_m - integer_n) + 1
    mean_val: float = total_sum / count_elements
    # Add 0.5 and then floor by integer division to simulate rounding
    rounded_result: int = int((mean_val + 0.5) // 1)  
    return bin(rounded_result)