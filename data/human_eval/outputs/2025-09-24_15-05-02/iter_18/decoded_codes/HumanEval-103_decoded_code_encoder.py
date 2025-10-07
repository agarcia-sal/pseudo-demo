from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation: int = 0
    for i in range(n, m + 1):
        summation += i
    avg: float = summation / (m - n + 1)
    rounded: int = round(avg)
    return bin(rounded)