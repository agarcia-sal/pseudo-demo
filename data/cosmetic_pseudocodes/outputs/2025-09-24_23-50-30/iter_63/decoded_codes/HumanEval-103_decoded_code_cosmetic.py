from typing import Union


def rounded_avg(n: int, m: int) -> Union[str, int]:
    if n > m:
        return -1
    total: int = 0
    current: int = n
    while current <= m:
        total += current
        current += 1
    average: float = total / (m - n + 1)
    rounded: int = round(average)
    binary_repr: str = bin(rounded)[2:]
    return binary_repr