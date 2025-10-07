from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if n > m:
        return -1
    total: int = 0
    count: int = m - n + 1
    for i in range(n, m + 1):
        total += i
    avg: float = total / count
    rounded: int = round(avg)
    bin_str: str = bin(rounded)
    return bin_str