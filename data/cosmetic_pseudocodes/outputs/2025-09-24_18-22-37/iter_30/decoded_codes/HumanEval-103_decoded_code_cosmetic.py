from typing import Union

def rounded_avg(p: int, q: int) -> Union[str, int]:
    if p > q:
        return -1
    total_sum = 0
    current = p
    while current <= q:
        total_sum += current
        current += 1
    count_elements = q - p + 1
    mean_calc = total_sum / count_elements
    rounded_mean = round(mean_calc)
    binary_str = bin(rounded_mean)[2:]  # Remove '0b' prefix
    return binary_str