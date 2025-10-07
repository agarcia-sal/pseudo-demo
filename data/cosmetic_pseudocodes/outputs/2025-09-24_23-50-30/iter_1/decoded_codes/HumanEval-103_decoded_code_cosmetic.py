from typing import Union


def rounded_avg(n: int, m: int) -> Union[str, int]:
    if not (m >= n):
        return -1
    total = 0
    count = m - n + 1
    current = n
    while current <= m:
        total += current
        current += 1
    result = total / count
    rounded_result = round(result)
    bin_result = bin(rounded_result)
    return bin_result