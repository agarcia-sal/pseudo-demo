from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1

    total_sum = sum(range(n, m + 1))
    average = total_sum / (m - n + 1)
    rounded_average = round(average)
    binary_result = bin(rounded_average)
    return binary_result