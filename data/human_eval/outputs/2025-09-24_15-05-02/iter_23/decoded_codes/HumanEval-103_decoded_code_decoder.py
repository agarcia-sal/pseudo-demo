from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation: int = 0
    for i in range(n, m + 1):
        summation += i
    length: int = m - n + 1
    average: float = summation / length
    rounded_average: int = round(average)
    return bin(rounded_average)