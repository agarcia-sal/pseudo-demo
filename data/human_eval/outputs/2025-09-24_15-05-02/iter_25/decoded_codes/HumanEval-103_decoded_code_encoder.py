from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    average = total_sum / count
    rounded_average = round(average)
    return bin(rounded_average)