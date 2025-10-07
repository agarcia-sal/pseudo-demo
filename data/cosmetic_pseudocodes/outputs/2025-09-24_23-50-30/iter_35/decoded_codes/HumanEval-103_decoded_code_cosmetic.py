from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if y < x:
        return -1
    total_sum = 0
    current_val = x
    while current_val <= y:
        total_sum += current_val
        current_val += 1
    count = (y - x) + 1
    mean_val = total_sum / count  # float division
    nearest_whole = int(mean_val + 0.5)  # rounding to nearest integer
    binary_str = bin(nearest_whole)[2:]  # binary representation without '0b'
    return binary_str