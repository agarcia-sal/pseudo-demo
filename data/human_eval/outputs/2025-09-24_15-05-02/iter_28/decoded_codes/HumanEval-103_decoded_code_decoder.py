from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation = sum(range(n, m + 1))
    average = summation / (m - n + 1)
    rounded_average = round(average)
    return bin(rounded_average)