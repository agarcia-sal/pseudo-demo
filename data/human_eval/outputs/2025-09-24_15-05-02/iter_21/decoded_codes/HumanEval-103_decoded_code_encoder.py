from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation: int = 0
    for i in range(n, m + 1):
        summation += i
    average: float = summation / (m - n + 1)
    rounded_average: int = round(average)
    binary_string: str = bin(rounded_average)
    return binary_string