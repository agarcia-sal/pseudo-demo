from typing import Union


def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    average = summation / (m - n + 1)
    rounded_average = round(average)
    return bin(rounded_average)