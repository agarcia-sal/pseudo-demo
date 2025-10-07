from typing import Union

def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1
    summation: int = sum(range(n, m + 1))
    average: float = summation / (m - n + 1)
    rounded_average: int = round(average)
    binary_representation: str = bin(rounded_average)
    return binary_representation