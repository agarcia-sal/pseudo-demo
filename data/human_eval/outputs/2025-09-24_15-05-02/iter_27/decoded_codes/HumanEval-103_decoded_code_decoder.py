from typing import Union


def rounded_avg(n: int, m: int) -> Union[str, int]:
    if m < n:
        return -1

    total_sum: int = sum(range(n, m + 1))
    count: int = m - n + 1
    average: float = total_sum / count
    rounded_average: int = round(average)
    binary_result: str = bin(rounded_average)

    return binary_result